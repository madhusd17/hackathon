"""
Lesson planner module.
Interacts with local Ollama LLM (qwen2.5:3b) to generate structured lesson JSON.
Enforces JSON Schema validation and seamlessly falls back to pre-built lessons so demos never fail.
"""

import json
import logging
import time
import requests
from jsonschema import validate
from core.fallbacks import get_fallback_lesson

logger = logging.getLogger(__name__)

LESSON_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "level": {"type": "string"},
        "language": {"type": "string"},
        "scenes": {
            "type": "array",
            "minItems": 3,
            "maxItems": 12,
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "enum": ["title_card", "diagram", "code_walkthrough", "quiz", "summary"]},
                    "heading": {"type": "string"},
                    "subheading": {"type": "string"},
                    "narration": {"type": "string"},
                    "code": {"type": "string"},
                    "highlight_lines": {"type": "array", "items": {"type": "integer"}},
                    "output": {"type": "string"},
                    "items": {"type": "array"},
                    "question": {"type": "string"},
                    "options": {"type": "array"},
                    "answer": {"type": "string"}
                },
                "required": ["type", "heading", "narration"]
            }
        }
    },
    "required": ["title", "level", "language", "scenes"]
}

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"

def generate_lesson_plan(topic: str, level: str = "beginner", language: str = "en", target_length: int = 45) -> tuple[dict, bool, float]:
    """
    Generates a lesson plan matching the hackathon schema.
    Returns: (lesson_json, used_fallback, elapsed_seconds)
    """
    t0 = time.time()

    # Plan roughly one presentation slide per 30 seconds, with room for level detail.
    base_scene_count = max(3, min(10, (target_length + 29) // 30))
    level_scene_bonus = 1 if level == "intermediate" else 0
    num_scenes = min(12, base_scene_count + level_scene_bonus)
    target_words = max(65, round(target_length * 2.1))
    language_names = {
        "en": "English",
        "hi": "Hindi",
        "ta": "Tamil",
        "te": "Telugu",
        "mr": "Marathi",
        "bn": "Bengali",
    }
    language_name = language_names.get(language, "English")
    prompt = f"""You are an educational video script planner.
Create a lesson specifically about the user's requested topic. Avoid generic filler and do not substitute a broader subject.
Topic: {topic}
Learner level: {level}
Write the lesson in English. The app will translate narration to {language_name} (language code: {language}).
Target video duration: {target_length} seconds
Create exactly {num_scenes} presentation slides (scenes) and about {target_words} words of narration in total.

Treat the scenes as a complete slide presentation. Give every slide a clear, specific heading, useful on-slide visual content, and narration that explains that slide. Use diagram scenes with 2-4 concise, topic-specific items to teach concepts; use code_walkthrough scenes with valid code and highlight_lines for programming; include concrete examples, applications, or a quiz when appropriate. Reserve the first slide for the introduction and the last slide for a recap. Do not fill the extra slides by repeating generic summaries.

For beginners, use everyday words, avoid unexplained technical terms, and explain any necessary new term simply. For intermediate learners, include appropriate technical vocabulary and briefly explain less familiar terms.
Every slide must contribute a different, topic-specific idea. The slide headings, visual items, examples, and narration must all teach the requested topic rather than generic filler.

Return ONLY one valid JSON object with this structure:
{{"title":"A topic-specific title","level":"{level}","language":"en","scenes":[{{"type":"title_card","heading":"Slide heading","narration":"Slide narration","subheading":"Optional","items":[{{"label":"Key idea","value":"Visible slide detail"}}],"code":"Optional code","highlight_lines":[1],"output":"Optional output","question":"Optional quiz question","options":["A","B"],"answer":"Optional correct answer"}}]}}
Use only scene types title_card, diagram, code_walkthrough, quiz, and summary. Include useful on-slide items for diagram and summary scenes. Include only relevant optional fields. Ensure the JSON is complete and has exactly {num_scenes} scenes."""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.35,
                    "num_predict": max(1400, min(4096, target_words * 5)),
                    "num_thread": 4,
                    "num_ctx": 8192
                }
            },
            timeout=120
        )
        if response.status_code == 200:
            raw_text = response.json().get("response", "").strip()
            start_idx = raw_text.find("{")
            end_idx = raw_text.rfind("}")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                plan = json.loads(raw_text[start_idx:end_idx + 1])
            else:
                plan = json.loads(raw_text)

            # Schema validation
            validate(instance=plan, schema=LESSON_SCHEMA)
            plan["topic"] = topic
            
            # If target language is non-English, handle translation
            if language != "en":
                plan = translate_lesson_plan(plan, language)
                
            elapsed = time.time() - t0
            return plan, False, elapsed
    except Exception as e:
        logger.warning(f"Ollama generation or validation failed ({e}), falling back to intelligent lesson generator.")

    # Graceful Fallback (Domain-aware dynamic lesson)
    fallback = get_fallback_lesson(topic, language=language, level=level)
    elapsed = time.time() - t0
    return fallback, True, elapsed


def translate_lesson_plan(plan: dict, target_lang: str) -> dict:
    """
    Translates headings and narration to the target language using local LLM or fallback.
    Maintains technical code and identifiers in English.
    """
    lang_names = {
        "hi": "Hindi (Devanagari script)",
        "ta": "Tamil (Tamil script)",
        "te": "Telugu (Telugu script)",
        "mr": "Marathi (Devanagari script)",
        "bn": "Bengali (Bengali script)"
    }
    target_name = lang_names.get(target_lang)
    if not target_name:
        return plan

    # Attempt fast sentence-by-sentence translation
    try:
        translated_scenes = []
        for sc in plan.get("scenes", []):
            sc_copy = dict(sc)
            narration = sc.get("narration", "")
            # Fast translate narration
            trans_prompt = f"Translate to {target_name} script only (keep code/technical terms in English, no explanation):\n{narration}"
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": trans_prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "num_predict": max(180, min(400, len(narration.split()) * 3)),
                        "num_thread": 4,
                        "num_ctx": 1024,
                    }
                },
                timeout=30
            )
            res.raise_for_status()
            if res.status_code == 200:
                translated_text = res.json().get("response", "").strip()
                if not translated_text:
                    raise ValueError("Translation returned empty narration.")
                sc_copy["narration"] = translated_text
            translated_scenes.append(sc_copy)
            
        plan["scenes"] = translated_scenes
        plan["language"] = target_lang
        return plan
    except Exception as e:
        logger.warning(f"Translation call failed: {e}")
        plan["language"] = "en"
        plan["translation_warning"] = "Local translation unavailable; English narration is shown."
        return plan
