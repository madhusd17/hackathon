import os
import time
import json
from core.planner import generate_lesson_plan
from core.tts_engine import tts_engine
from core.video_renderer import export_lesson_mp4
from core.cache_manager import save_to_cache, get_cache_key

test_topics = [
    {
        "topic": "How a Python loop works",
        "lang": "en",
        "voice": "hf_alpha",
        "out_dir": "output/submission_lesson_en"
    },
    {
        "topic": "Photosynthesis",
        "lang": "hi",
        "voice": "hf_alpha",
        "out_dir": "output/submission_lesson_hi"
    }
]

for t in test_topics:
    topic = t["topic"]
    lang = t["lang"]
    voice = t["voice"]
    out_dir = t["out_dir"]
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n==========================================")
    print(f"Generating Lesson for '{topic}' [{lang}]...")
    print(f"==========================================")
    
    t0 = time.time()
    # 1. Plan
    plan, used_fb, plan_time = generate_lesson_plan(topic, language=lang)
    title_safe = plan.get('title', '').encode('ascii', 'replace').decode()
    print(f"1. Plan generated in {plan_time:.2f}s (Used Fallback: {used_fb})")
    print(f"   Title: {title_safe} ({len(plan.get('scenes', []))} scenes)")

    # 2. TTS
    enriched, srt_path, tts_time = tts_engine.synthesize_lesson(
        lesson=plan,
        output_dir=out_dir,
        voice=voice,
        speed=1.0
    )
    print(f"2. Audio synthesized in {tts_time:.2f}s (Total duration: {enriched['total_duration']}s)")
    print(f"   SRT saved to: {srt_path}")

    # 3. Video Render & MP4 Export
    mp4_path, vid_time = export_lesson_mp4(enriched, out_dir)
    print(f"3. MP4 exported in {vid_time:.2f}s")
    print(f"   Final MP4: {mp4_path} (Size: {os.path.getsize(mp4_path):,} bytes)")

    # 4. Save to cache
    key = get_cache_key(topic, lang, "beginner", voice)
    save_to_cache(key, enriched, out_dir)
    print(f"4. Cached with key: {key}")
    print(f"Total time: {time.time() - t0:.2f}s")

print("\nALL SUBMISSION LESSONS GENERATED SUCCESSFULLY!")
