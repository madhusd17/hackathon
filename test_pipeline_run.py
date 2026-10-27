import os
import subprocess
import time
import kokoro_onnx
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

kokoro_model = r"C:\Users\dell\Downloads\kokoro-v1.0.onnx"
voices_path = r"C:\Users\dell\Downloads\voices-v1.0.bin"
kokoro = kokoro_onnx.Kokoro(kokoro_model, voices_path)

os.makedirs("test_pipeline", exist_ok=True)

font_path = r"C:\Windows\Fonts\NirmalaB.ttf"
font_regular = r"C:\Windows\Fonts\Nirmala.ttf"

scenes = [
    {
        "heading": "Step 1: Introduction to Loops",
        "type": "title_card",
        "narration": "A loop repeats an action multiple times automatically.",
        "lang": "en-us",
        "voice": "hf_alpha"
    },
    {
        "heading": "चरण २: कोड समझना",
        "type": "code_walkthrough",
        "narration": "यह लूप शून्य से दो तक गिनती करता है।",
        "code": "for i in range(3):\n    print(i)",
        "lang": "hi",
        "voice": "hf_alpha"
    }
]

scene_mp4s = []

for idx, sc in enumerate(scenes):
    t0 = time.time()
    # 1. Synthesize audio
    wav_path = f"test_pipeline/audio_{idx}.wav"
    samples, sr = kokoro.create(sc["narration"], voice=sc["voice"], speed=1.0, lang=sc["lang"])
    # Add 0.5s silence at end
    silence_samples = int(sr * 0.5)
    import numpy as np
    padded_samples = np.concatenate([samples, np.zeros(silence_samples, dtype=samples.dtype)])
    sf.write(wav_path, padded_samples, sr)
    dur = len(padded_samples) / sr
    print(f"Scene {idx} audio duration: {dur:.2f}s (generated in {time.time()-t0:.2f}s)")

    # 2. Render 1280x720 frame
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([(0, 0), (1280, 80)], fill=(30, 41, 59))
    title_font = ImageFont.truetype(font_path, 32)
    draw.text((40, 22), "Blu Visual Teacher", fill=(56, 189, 248), font=title_font)
    badge_font = ImageFont.truetype(font_regular, 20)
    draw.text((1050, 28), f"Scene {idx+1} of {len(scenes)}", fill=(148, 163, 184), font=badge_font)

    # Main content
    heading_font = ImageFont.truetype(font_path, 42)
    draw.text((80, 140), sc["heading"], fill=(255, 255, 255), font=heading_font)

    if sc.get("code"):
        # Draw code card
        draw.rounded_rectangle([(80, 220), (1200, 480)], radius=16, fill=(2, 6, 23), outline=(51, 65, 85), width=2)
        code_font = ImageFont.truetype(font_regular, 28)
        draw.text((110, 260), sc["code"], fill=(134, 239, 172), font=code_font)

    # Captions bar
    draw.rectangle([(0, 620), (1280, 720)], fill=(2, 6, 23))
    caption_font = ImageFont.truetype(font_path, 24)
    draw.text((60, 645), f"🎙️  {sc['narration']}", fill=(241, 245, 249), font=caption_font)

    img_path = f"test_pipeline/frame_{idx}.png"
    img.save(img_path)

    # 3. Create scene MP4 with FFmpeg
    scene_mp4 = f"test_pipeline/scene_{idx}.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", img_path,
        "-i", wav_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        scene_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    scene_mp4s.append(scene_mp4)

# 4. Concatenate scenes
list_file = "test_pipeline/concat_list.txt"
with open(list_file, "w", encoding="utf-8") as f:
    for m in scene_mp4s:
        # relative forward slashes
        f.write(f"file '{os.path.basename(m)}'\n")

final_mp4 = "test_pipeline/final_lesson.mp4"
concat_cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", list_file,
    "-c", "copy",
    final_mp4
]
subprocess.run(concat_cmd, check=True, cwd="test_pipeline", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("SUCCESS! Final MP4 created at:", final_mp4, "Size:", os.path.getsize(final_mp4))

