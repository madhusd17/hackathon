"""
Blu Visual Teacher - Offline Local Video Generation Server
Built for CPU laptops, 100% offline, zero external APIs.
"""

import os
import time
import uuid
import logging
import math
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from werkzeug.exceptions import HTTPException
from core.planner import generate_lesson_plan, translate_lesson_plan
from core.tts_engine import tts_engine
from core.video_renderer import export_lesson_mp4, render_scene_frame
from core.cache_manager import get_cache_key, get_cached_lesson, save_to_cache, list_cached_lessons

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("blu-teacher")

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.errorhandler(HTTPException)
def handle_http_error(error):
    if request.path.startswith("/api/"):
        return jsonify({"success": False, "error": error.description}), error.code
    return error


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CACHE_DIR = os.path.join(BASE_DIR, "cache")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)


@app.route("/")
def index():
    """Renders the main web application."""
    return render_template("index.html")


@app.route("/api/generate_full_lesson", methods=["POST"])
def generate_full_lesson():
    """
    Executes all stages end-to-end:
    Topic in -> Lesson Plan -> Kokoro Narration -> Synced Video & 720p MP4.
    """
    total_t0 = time.time()
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"success": False, "error": "Request body must be a JSON object."}), 400

    raw_topic = data.get("topic", "How a Python loop works")
    if not isinstance(raw_topic, str) or not raw_topic.strip():
        return jsonify({"success": False, "error": "Enter a lesson topic before generating."}), 400
    topic = raw_topic.strip()
    level = data.get("level", "beginner")
    language = data.get("language", "en")
    voice = data.get("voice", "hf_alpha")
    try:
        speed = float(data.get("speed", 1.0))
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "Speech speed must be a number."}), 400
    if not math.isfinite(speed) or not 0.8 <= speed <= 1.3:
        return jsonify({"success": False, "error": "Speech speed must be between 0.8x and 1.3x."}), 400
    raw_target_length = data.get("target_length", 45)
    if isinstance(raw_target_length, bool) or (
        isinstance(raw_target_length, float) and not raw_target_length.is_integer()
    ):
        return jsonify({"success": False, "error": "Video duration must be between 30 and 300 seconds."}), 400
    try:
        target_length = int(raw_target_length)
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "Video duration must be between 30 and 300 seconds."}), 400
    if not 30 <= target_length <= 300:
        return jsonify({"success": False, "error": "Video duration must be between 30 and 300 seconds."}), 400
    force_refresh = bool(data.get("force_refresh", False))

    cache_key = get_cache_key(topic, language, level, voice, speed, target_length)
    
    # Check cache if not forcing refresh
    if not force_refresh:
        cached = get_cached_lesson(cache_key)
        if cached:
            cached_topic = " ".join(str(cached.get("topic", "")).split()).casefold()
            if cached_topic == " ".join(topic.split()).casefold():
                return jsonify({
                    "success": True,
                    "cached": True,
                    "lesson": cached,
                    "folder": f"cache/{cache_key}",
                    "metrics": {
                        "planner_s": 0.01,
                        "tts_s": 0.01,
                        "video_s": 0.01,
                        "total_s": round(time.time() - total_t0, 2),
                        "used_fallback": bool(cached.get("used_fallback", False)),
                        "translation_warning": cached.get("translation_warning"),
                        "target_duration": cached.get("target_duration", target_length),
                        "actual_duration": cached.get("total_duration", 0)
                    }
                })
            logger.warning(
                "Ignoring cache entry %s because its topic does not match request %r.",
                cache_key,
                topic,
            )

    missing_tts_assets = [
        path for path in (tts_engine.model_path, tts_engine.voices_path)
        if not os.path.isfile(path)
    ]
    if missing_tts_assets:
        return jsonify({
            "success": False,
            "error": (
                "The narration model files are missing. Add the Kokoro ONNX model and "
                f"voice file at these paths, then try again: {', '.join(missing_tts_assets)}"
            ),
        }), 503

    # Unique job output folder
    job_id = f"lesson_{uuid.uuid4().hex[:8]}"
    job_dir = os.path.join(OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    try:
        # 1. Lesson Planning (Ollama / Fallback)
        plan, used_fallback, planner_s = generate_lesson_plan(
            topic=topic,
            level=level,
            language=language,
            target_length=target_length,
            speed=speed
        )

        # 2. Local Narration & Duration calculation (Kokoro)
        enriched_lesson, srt_path, tts_s = tts_engine.synthesize_lesson(
            lesson=plan,
            output_dir=job_dir,
            voice=voice,
            speed=speed,
            target_duration=target_length,
        )

        # 3. 720p MP4 Video Assembly (Pillow + FFmpeg)
        final_mp4_path, video_s = export_lesson_mp4(enriched_lesson, job_dir)

        total_s = round(time.time() - total_t0, 2)
        enriched_lesson["job_id"] = job_id
        enriched_lesson["voice"] = voice
        enriched_lesson["speed"] = speed
        enriched_lesson["target_duration"] = target_length
        enriched_lesson["used_fallback"] = used_fallback

        # Save to Cache
        save_to_cache(cache_key, enriched_lesson, job_dir)
    except Exception as error:
        logger.exception("Lesson generation failed for topic %r.", topic)
        return jsonify({
            "success": False,
            "error": f"Lesson generation failed: {error}",
        }), 500

    return jsonify({
        "success": True,
        "cached": False,
        "lesson": enriched_lesson,
        "folder": f"output/{job_id}",
        "metrics": {
            "planner_s": round(planner_s, 2),
            "tts_s": round(tts_s, 2),
            "video_s": round(video_s, 2),
            "total_s": total_s,
            "used_fallback": used_fallback,
            "translation_warning": enriched_lesson.get("translation_warning"),
            "target_duration": target_length,
            "actual_duration": enriched_lesson.get("total_duration", 0)
        }
    })


@app.route("/api/revoice", methods=["POST"])
def revoice_lesson():
    """
    Bonus Feature:
    Re-voices a finished lesson into another language without re-planning the scenes!
    """
    t0 = time.time()
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"success": False, "error": "Invalid request data"}), 400

    lesson = data.get("lesson")
    new_lang = data.get("new_language", "hi")
    new_voice = data.get("new_voice", "hf_alpha")
    speed = float(data.get("speed", 1.0))

    if not lesson or "scenes" not in lesson:
        return jsonify({"success": False, "error": "Invalid lesson data"}), 400

    # Translate narration & headings to new language
    translated_lesson = translate_lesson_plan(lesson, new_lang)
    translated_lesson["language"] = new_lang

    job_id = f"revoice_{uuid.uuid4().hex[:8]}"
    job_dir = os.path.join(OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    # Re-synthesize audio
    enriched_lesson, srt_path, tts_s = tts_engine.synthesize_lesson(
        lesson=translated_lesson,
        output_dir=job_dir,
        voice=new_voice,
        speed=speed
    )

    # Re-export 720p MP4
    final_mp4_path, video_s = export_lesson_mp4(enriched_lesson, job_dir)

    return jsonify({
        "success": True,
        "lesson": enriched_lesson,
        "folder": f"output/{job_id}",
        "metrics": {
            "planner_s": 0.0,
            "tts_s": round(tts_s, 2),
            "video_s": round(video_s, 2),
            "total_s": round(time.time() - t0, 2)
        }
    })


@app.route("/api/edit_scene", methods=["POST"])
def edit_scene():
    """
    Bonus Feature:
    Allows teacher to edit a scene's text/code/narration and regenerate only that scene.
    """
    t0 = time.time()
    data = request.json or {}
    lesson = data.get("lesson")
    scene_idx = data.get("scene_index", 0)
    updated_scene = data.get("updated_scene")

    if (
        not isinstance(lesson, dict)
        or not isinstance(lesson.get("scenes"), list)
        or not isinstance(scene_idx, int)
        or isinstance(scene_idx, bool)
        or scene_idx < 0
        or scene_idx >= len(lesson["scenes"])
        or not isinstance(updated_scene, dict)
    ):
        return jsonify({"success": False, "error": "Invalid lesson or scene data"}), 400

    if any(
        not isinstance(scene, dict)
        or (
            index != scene_idx
            and (
                not isinstance(scene.get("duration"), (int, float))
                or isinstance(scene.get("duration"), bool)
                or not math.isfinite(scene["duration"])
            )
        )
        for index, scene in enumerate(lesson["scenes"])
    ):
        return jsonify({"success": False, "error": "Invalid lesson scene data"}), 400

    job_id = lesson.get("job_id", f"edit_{uuid.uuid4().hex[:6]}")
    job_dir = os.path.join(OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    lesson["scenes"][scene_idx] = updated_scene

    # Re-synthesize this scene only
    wav_path = os.path.join(job_dir, f"scene_{scene_idx}.wav")
    new_dur = tts_engine.synthesize_scene(
        text=updated_scene.get("narration", ""),
        output_wav_path=wav_path,
        voice=lesson.get("voice", "hf_alpha"),
        language=lesson.get("language", "en"),
        speed=float(lesson.get("speed", 1.0))
    )
    updated_scene["duration"] = round(new_dur, 2)

    # Recalculate timeline
    cur = 0.0
    for sc in lesson["scenes"]:
        sc["start_time"] = round(cur, 2)
        cur += sc["duration"]
        sc["end_time"] = round(cur, 2)
    lesson["total_duration"] = round(cur, 2)

    # Re-export video
    final_mp4_path, video_s = export_lesson_mp4(lesson, job_dir)

    return jsonify({
        "success": True,
        "lesson": lesson,
        "folder": f"output/{job_id}",
        "metrics": {
            "total_s": round(time.time() - t0, 2)
        }
    })


@app.route("/api/load_cache/<key>")
def load_cache_by_key(key):
    """Loads a cached lesson directly by its hash key."""
    cached = get_cached_lesson(key)
    if cached:
        return jsonify({
            "success": True,
            "cached": True,
            "lesson": cached,
            "folder": f"cache/{key}",
            "metrics": {
                "planner_s": 0.01,
                "tts_s": 0.01,
                "video_s": 0.01,
                "total_s": 0.01,
                "used_fallback": False
            }
        })
    return jsonify({"success": False, "error": "Not found in cache"}), 404


@app.route("/api/cached_lessons", methods=["GET"])
def get_cached_lessons():
    """Returns library of cached lessons."""
    return jsonify({"lessons": list_cached_lessons()})


@app.route("/media/<path:filepath>")
def serve_media(filepath):
    """Serves media files (WAV, PNG, MP4, SRT) supporting nested paths."""
    full_path = os.path.join(BASE_DIR, filepath)
    dir_name = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)
    return send_from_directory(dir_name, file_name)


@app.route("/api/download/<path:filepath>")
def download_media(filepath):
    """Downloads artifact with proper attachment header supporting nested paths."""
    full_path = os.path.join(BASE_DIR, filepath)
    dir_name = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)
    return send_from_directory(dir_name, file_name, as_attachment=True)


if __name__ == "__main__":
    # Warm up TTS on startup
    try:
        tts_engine.initialize()
    except Exception as e:
        logger.warning(f"Could not warm up TTS immediately: {e}")
    app.run(host="127.0.0.1", port=5000, debug=False)
