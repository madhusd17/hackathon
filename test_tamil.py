import os
from core.fallbacks import get_fallback_lesson
from core.tts_engine import tts_engine
from core.video_renderer import export_lesson_mp4

out_dir = "output/submission_lesson_ta"
os.makedirs(out_dir, exist_ok=True)
plan = get_fallback_lesson("python loops", language="ta")
enriched, srt, tts_time = tts_engine.synthesize_lesson(plan, out_dir, voice="hf_alpha")
mp4, vid_time = export_lesson_mp4(enriched, out_dir)
print(f"Tamil lesson generated! Duration: {enriched['total_duration']}s, MP4 size: {os.path.getsize(mp4):,} bytes")

