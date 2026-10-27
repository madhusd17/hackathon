"""
Lesson planner module.
Interacts with local Ollama LLM (qwen2.5:3b) to generate structured lesson JSON.
Enforces JSON Schema validation and seamlessly falls back to pre-built lessons so demos never fail.
"""

import json
import logging
import time
import requests
from jsonschema import validate, ValidationError
from core.fallbacks import get_fallback_lesson, get_curated_fallback

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

    # 1. Check curated library for instant, high-quality pedagogical lessons
    curated = get_curated_fallback(topic, language=language)
    if curated:
        elapsed = time.time() - t0
        return curated, False, elapsed

    # 2. For custom topics, prompt local LLM (Ollama qwen2.5:3b)
    num_scenes = 3 if target_length <= 40 else 4
    prompt = f"""You are an educational video script planner.
Create a concise, structured visual lesson plan for school students.
Topic: {topic}
Learner Level: {level}
Language: en
Target Scene Count: {num_scenes}

Rules:
1. Output ONLY a valid JSON object matching this exact schema:
{{
  "title": "{topic.title()}",
  "level": "{level}",
  "language": "en",
  "scenes": [
    {{
      "type": "title_card",
      "heading": "Introduction to {topic}",
      "subheading": "Core concept simplified",
      "narration": "A one or two sentence clear explanation."
    }},
    {{
      "type": "diagram",
      "heading": "Step 1: How It Operates",
      "items": [
        {{"label": "Step 1", "value": "First action"}},
        {{"label": "Step 2", "value": "Second action"}},
        {{"label": "Step 3", "value": "Final outcome"}}
      ],
      "narration": "Clear narration explaining each step."
    }},
    {{
      "type": "summary",
      "heading": "Step 2: Key Takeaways",
      "items": [
        {{"label": "Fact 1", "value": "Summary point one"}},
        {{"label": "Fact 2", "value": "Summary point two"}}
      ],
      "narration": "Conclusive summary reinforcing learning."
    }}
  ]
}}
2. If the topic involves programming or code, use 'code_walkthrough' with 'code' and 'highlight_lines' for scene 2.
3. No markdown, no conversation, only the raw JSON.
Output valid JSON:"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.2,
                    "num_predict": 300,
                    "num_thread": 4,
                    "num_ctx": 1024
                }
            },
            timeout=25
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

    # Check if a curated lesson exists for this topic in target language
    topic = plan.get("topic", plan.get("title", ""))
    curated = get_curated_fallback(topic, language=target_lang)
    if curated and curated.get("language") == target_lang:
        return curated

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
            if res.status_code == 200:
                translated_text = res.json().get("response", "").strip()
                if translated_text:
                    sc_copy["narration"] = translated_text
            translated_scenes.append(sc_copy)
            
        plan["scenes"] = translated_scenes
        plan["language"] = target_lang
        return plan
    except Exception as e:
        logger.warning(f"Translation call failed: {e}")

    # If translation call fails, use dynamic fallback in target language
    return get_fallback_lesson(topic, language=target_lang, level=plan.get("level", "beginner"))
