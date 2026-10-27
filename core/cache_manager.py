"""
Cache manager for lesson plans, generated audio, and MP4 videos.
Ensures instant replay and zero redundant computation.
"""

import os
import json
import hashlib
import shutil
import logging

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, "cache")


def get_cache_key(topic: str, language: str, level: str, voice: str = "hf_alpha") -> str:
    """Generates a stable cache key string."""
    raw = f"{topic.strip().lower()}_{language.strip().lower()}_{level.strip().lower()}_{voice.strip().lower()}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]


def get_cached_lesson(key: str) -> dict | None:
    """Retrieves cached lesson metadata if it exists."""
    target_dir = os.path.join(CACHE_DIR, key)
    plan_file = os.path.join(target_dir, "lesson_plan.json")
    mp4_file = os.path.join(target_dir, "lesson.mp4")

    if os.path.exists(plan_file) and os.path.exists(mp4_file):
        try:
            with open(plan_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["cached"] = True
            data["cache_key"] = key
            return data
        except Exception as e:
            logger.warning(f"Error reading cache {key}: {e}")
    return None


def save_to_cache(key: str, lesson_data: dict, work_dir: str):
    """Copies output artifacts into cache folder."""
    target_dir = os.path.join(CACHE_DIR, key)
    os.makedirs(target_dir, exist_ok=True)
    
    # Save plan
    plan_file = os.path.join(target_dir, "lesson_plan.json")
    with open(plan_file, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)

    # Copy files
    for item in os.listdir(work_dir):
        src = os.path.join(work_dir, item)
        dst = os.path.join(target_dir, item)
        if os.path.isfile(src):
            shutil.copy2(src, dst)


def list_cached_lessons() -> list[dict]:
    """Lists all cached lessons for the UI library."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    results = []
    for item in os.listdir(CACHE_DIR):
        plan_path = os.path.join(CACHE_DIR, item, "lesson_plan.json")
        if os.path.exists(plan_path):
            try:
                with open(plan_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                results.append({
                    "cache_key": item,
                    "title": data.get("title", "Untitled"),
                    "topic": data.get("topic", ""),
                    "language": data.get("language", "en"),
                    "level": data.get("level", "beginner"),
                    "scenes_count": len(data.get("scenes", [])),
                    "total_duration": data.get("total_duration", 0)
                })
            except Exception:
                pass
    return results

