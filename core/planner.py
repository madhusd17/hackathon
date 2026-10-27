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
            "minItems": 2,
            "maxItems": 6,
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

    # Keep lessons short at the minimum duration and add slides for longer requests.
    base_scene_count = max(2, min(6, round(target_length / 50)))
    level_scene_bonus = 1 if level == "intermediate" else 0
    num_scenes = min(6, base_scene_count + level_scene_bonus)
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
Create exactly {num_scenes} distinct scenes and about {target_words} words of narration in total.

Use an engaging progression: introduce the exact topic, explain its important parts, give a relevant example or application, then recap. Use a code_walkthrough scene for programming topics and include valid code and highlight_lines. Use diagram scenes for processes and concepts. Include a short quiz when there are enough scenes.

For beginners, use everyday words, avoid unexplained technical terms, and explain any necessary new term simply. For intermediate learners, include appropriate technical vocabulary and briefly explain less familiar terms.
Every scene must contribute a different, topic-specific idea. Do not repeat the same generic steps across topics.

Return ONLY one valid JSON object with this structure:
{{"title":"A topic-specific title","level":"{level}","language":"en","scenes":[{{"type":"title_card","heading":"Scene heading","narration":"Spoken explanation","subheading":"Optional","items":[{{"label":"Label","value":"Detail"}}],"code":"Optional code","highlight_lines":[1],"output":"Optional output","question":"Optional quiz question","options":["A","B"],"answer":"Optional correct answer"}}]}}
Use only scene types title_card, diagram, code_walkthrough, quiz, and summary. Include only relevant optional fields. Ensure the JSON is complete and has exactly {num_scenes} scenes."""

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
                    "num_predict": max(900, min(2400, target_words * 4)),
                    "num_thread": 4,
                    "num_ctx": 4096
                }
            },
            timeout=60
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
            # Fast translate narration
            trans_prompt = f"Translate to {target_name} script only (keep code/technical terms in English, no explanation):\n{sc['narration']}"
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": trans_prompt,
                    "stream": False,
                    "options": {"temperature": 0.1, "num_predict": 100, "num_thread": 4, "num_ctx": 512}
                },
                timeout=10
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
