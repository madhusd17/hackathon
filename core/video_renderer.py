"""
Video Renderer Module.
Generates 1280x720 graphic cards for scenes using Pillow + Nirmala font (supporting all Indian scripts).
Combines frames and narration audio into high-quality 720p MP4 video with FFmpeg.
"""

import os
import subprocess
import time
import logging
from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_BOLD = os.path.join(BASE_DIR, "fonts", "NirmalaB.ttf")
FONT_REGULAR = os.path.join(BASE_DIR, "fonts", "Nirmala.ttf")

# Fallback to system fonts if not in local directory
if not os.path.exists(FONT_BOLD):
    FONT_BOLD = r"C:\Windows\Fonts\NirmalaB.ttf"
if not os.path.exists(FONT_REGULAR):
    FONT_REGULAR = r"C:\Windows\Fonts\Nirmala.ttf"


def get_fonts():
    """Loads fonts with various sizes."""
    try:
        return {
            "title": ImageFont.truetype(FONT_BOLD, 46),
            "heading": ImageFont.truetype(FONT_BOLD, 36),
            "subheading": ImageFont.truetype(FONT_REGULAR, 26),
            "body": ImageFont.truetype(FONT_REGULAR, 24),
            "code": ImageFont.truetype(FONT_REGULAR, 26),
            "badge": ImageFont.truetype(FONT_BOLD, 20),
            "caption": ImageFont.truetype(FONT_REGULAR, 24)
        }
    except Exception as e:
        logger.warning(f"Error loading Nirmala font: {e}, falling back to default.")
        default = ImageFont.load_default()
        return {k: default for k in ["title", "heading", "subheading", "body", "code", "badge", "caption"]}


def draw_header(draw, title: str, step_str: str, fonts: dict):
    """Draws sleek top navigation bar."""
    draw.rectangle([(0, 0), (1280, 80)], fill=(30, 41, 59))
    # Brand
    draw.text((45, 24), "Blu Visual Teacher", fill=(56, 189, 248), font=fonts["heading"])
    # Topic
    draw.text((460, 28), title, fill=(226, 232, 240), font=fonts["subheading"])
    # Step indicator pill
    draw.rounded_rectangle([(1080, 20), (1235, 60)], radius=20, fill=(51, 65, 85))
    draw.text((1100, 28), step_str, fill=(148, 163, 184), font=fonts["badge"])


def draw_caption_bar(draw, narration: str, fonts: dict):
    """Draws bottom caption container."""
    draw.rectangle([(0, 610), (1280, 720)], fill=(15, 23, 42))
    draw.line([(0, 610), (1280, 610)], fill=(51, 65, 85), width=2)
    # Narration pill
    draw.rounded_rectangle([(40, 625), (1240, 705)], radius=12, fill=(30, 41, 59))
    draw.text((65, 648), f"🎙️  {narration}", fill=(241, 245, 249), font=fonts["caption"])


def render_title_card(scene: dict, lesson_title: str, step_str: str, fonts: dict) -> Image.Image:
    """Renders Title Card Scene."""
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw_header(draw, lesson_title, step_str, fonts)

    # Center Hero Card
    draw.rounded_rectangle([(100, 150), (1180, 560)], radius=24, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
    
    # Topic tag
    draw.rounded_rectangle([(140, 190), (320, 235)], radius=12, fill=(14, 116, 144))
    draw.text((160, 200), "CONCEPT LESSON", fill=(224, 242, 254), font=fonts["badge"])

    # Main Heading
    heading = scene.get("heading", lesson_title)
    draw.text((140, 270), heading, fill=(255, 255, 255), font=fonts["title"])

    # Subheading
    subheading = scene.get("subheading", "")
    if subheading:
        draw.text((140, 360), subheading, fill=(148, 163, 184), font=fonts["subheading"])

    # Visual graphic icon
    draw.ellipse([(930, 220), (1110, 400)], fill=(15, 23, 42), outline=(56, 189, 248), width=3)
    draw.text((990, 280), "💡", fill=(250, 204, 21), font=fonts["title"])

    draw_caption_bar(draw, scene.get("narration", ""), fonts)
    return img


def render_diagram_card(scene: dict, lesson_title: str, step_str: str, fonts: dict) -> Image.Image:
    """Renders Diagram / Flowchart Scene with labels and connecting arrows."""
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw_header(draw, lesson_title, step_str, fonts)

    # Scene Heading
    draw.text((70, 115), scene.get("heading", "Visual Diagram"), fill=(255, 255, 255), font=fonts["heading"])

    # Items / Nodes
    raw_items = scene.get("items", [])
    items = []
    for it in raw_items:
        if isinstance(it, dict):
            items.append((it.get("label", "Step"), it.get("value", "")))
        elif isinstance(it, str):
            parts = it.split(":", 1)
            if len(parts) == 2:
                items.append((parts[0].strip(), parts[1].strip()))
            else:
                items.append(("Step", it.strip()))

    num_items = max(1, len(items))
    card_width = min(320, int(1120 / num_items) - 30)
    card_height = 280
    start_x = 70
    spacing = int((1140 - (card_width * num_items)) / max(1, (num_items - 1))) if num_items > 1 else 0

    colors = [
        ((30, 41, 59), (56, 189, 248)),   # Blue
        ((30, 41, 59), (52, 211, 153)),   # Green
        ((30, 41, 59), (251, 191, 36)),   # Amber
        ((30, 41, 59), (168, 85, 247))    # Purple
    ]

    for i, (label, val) in enumerate(items):
        cx = start_x + i * (card_width + spacing)
        cy = 190
        bg_col, border_col = colors[i % len(colors)]
        
        # Node Box
        draw.rounded_rectangle([(cx, cy), (cx + card_width, cy + card_height)], radius=16, fill=bg_col, outline=border_col, width=2)
        
        # Step Number Badge
        draw.rounded_rectangle([(cx + 20, cy + 20), (cx + card_width - 20, cy + 65)], radius=10, fill=(15, 23, 42))
        draw.text((cx + 35, cy + 30), f"#{i+1} {label}", fill=border_col, font=fonts["badge"])

        # Value text (wrapped)
        words = val.split()
        line = ""
        ly = cy + 90
        for w in words:
            if len(line + " " + w) > 22:
                draw.text((cx + 25, ly), line, fill=(241, 245, 249), font=fonts["body"])
                ly += 35
                line = w
            else:
                line = line + " " + w if line else w
        if line:
            draw.text((cx + 25, ly), line, fill=(241, 245, 249), font=fonts["body"])

        # Arrow to next node
        if i < num_items - 1:
            arrow_x = cx + card_width + 8
            arrow_y = cy + card_height // 2
            draw.line([(arrow_x, arrow_y), (arrow_x + spacing - 16, arrow_y)], fill=(148, 163, 184), width=4)
            # Arrow head
            draw.polygon([
                (arrow_x + spacing - 14, arrow_y),
                (arrow_x + spacing - 26, arrow_y - 8),
                (arrow_x + spacing - 26, arrow_y + 8)
            ], fill=(148, 163, 184))

    draw_caption_bar(draw, scene.get("narration", ""), fonts)
    return img


def render_code_card(scene: dict, lesson_title: str, step_str: str, fonts: dict) -> Image.Image:
    """Renders Code Walkthrough Scene with IDE styling."""
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw_header(draw, lesson_title, step_str, fonts)

    # Heading
    draw.text((70, 105), scene.get("heading", "Code Walkthrough"), fill=(255, 255, 255), font=fonts["heading"])

    # IDE Window Card
    draw.rounded_rectangle([(70, 160), (1210, 580)], radius=16, fill=(2, 6, 23), outline=(51, 65, 85), width=2)
    # IDE top bar
    draw.rounded_rectangle([(70, 160), (1210, 205)], radius=14, fill=(15, 23, 42))
    # MacOS style dots
    draw.ellipse([(95, 178), (107, 190)], fill=(239, 68, 68))    # red
    draw.ellipse([(117, 178), (129, 190)], fill=(234, 179, 8))   # yellow
    draw.ellipse([(139, 178), (151, 190)], fill=(34, 197, 94))   # green
    draw.text((180, 173), "script.py - Visual Python Engine", fill=(148, 163, 184), font=fonts["badge"])

    code = scene.get("code", "for i in range(3):\n    print(i)")
    code_lines = code.split("\n")
    highlight_lines = scene.get("highlight_lines", [1])

    y_code = 230
    for idx, line in enumerate(code_lines, start=1):
        is_highlighted = idx in highlight_lines
        if is_highlighted:
            # Highlight glow strip
            draw.rectangle([(72, y_code - 5), (1208, y_code + 35)], fill=(30, 41, 59))
            draw.rectangle([(72, y_code - 5), (78, y_code + 35)], fill=(56, 189, 248))

        # Line number
        draw.text((100, y_code), f"{idx:2d}", fill=(100, 116, 139), font=fonts["code"])
        # Code line
        line_color = (134, 239, 172) if is_highlighted else (241, 245, 249)
        draw.text((150, y_code), line, fill=line_color, font=fonts["code"])
        y_code += 42

    # Terminal output box
    output_text = scene.get("output", "")
    if output_text:
        draw.rounded_rectangle([(100, 440), (1180, 550)], radius=10, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.text((120, 450), "Output Terminal:", fill=(148, 163, 184), font=fonts["badge"])
        out_lines = output_text.split("\n")
        oy = 480
        for ol in out_lines[:2]:
            draw.text((130, oy), f"> {ol}", fill=(56, 189, 248), font=fonts["code"])
            oy += 32

    draw_caption_bar(draw, scene.get("narration", ""), fonts)
    return img


def render_quiz_card(scene: dict, lesson_title: str, step_str: str, fonts: dict) -> Image.Image:
    """Renders Interactive Quiz Scene."""
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw_header(draw, lesson_title, step_str, fonts)

    # Heading
    draw.text((70, 105), scene.get("heading", "Quick Knowledge Check"), fill=(255, 255, 255), font=fonts["heading"])

    # Question Box
    draw.rounded_rectangle([(70, 160), (1210, 240)], radius=16, fill=(30, 41, 59), outline=(168, 85, 247), width=2)
    question = scene.get("question", "What is the result?")
    draw.text((100, 185), f"❓  {question}", fill=(241, 245, 249), font=fonts["subheading"])

    options = scene.get("options", ["A", "B", "C", "D"])
    answer = scene.get("answer", "")

    # Draw 4 option buttons
    coords = [
        ((70, 260), (620, 370)),
        ((660, 260), (1210, 370)),
        ((70, 400), (620, 510)),
        ((660, 400), (1210, 510))
    ]
    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(options[:4]):
        (x1, y1), (x2, y2) = coords[i]
        is_answer = str(opt).strip() == str(answer).strip()
        bg_col = (16, 185, 129, 40) if is_answer else (30, 41, 59)
        border_col = (52, 211, 153) if is_answer else (51, 65, 85)
        text_col = (52, 211, 153) if is_answer else (226, 232, 240)

        draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=12, fill=bg_col, outline=border_col, width=2)
        # Option Badge
        draw.ellipse([(x1 + 20, y1 + 30), (x1 + 65, y1 + 75)], fill=(15, 23, 42), outline=border_col, width=2)
        draw.text((x1 + 35, y1 + 40), labels[i], fill=border_col, font=fonts["badge"])
        # Option text
        draw.text((x1 + 85, y1 + 42), str(opt), fill=text_col, font=fonts["body"])

        if is_answer:
            draw.text((x2 - 130, y1 + 42), "✓ Correct", fill=(52, 211, 153), font=fonts["badge"])

    draw_caption_bar(draw, scene.get("narration", ""), fonts)
    return img


def render_summary_card(scene: dict, lesson_title: str, step_str: str, fonts: dict) -> Image.Image:
    """Renders Summary / Recap Scene."""
    img = Image.new("RGB", (1280, 720), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    draw_header(draw, lesson_title, step_str, fonts)

    # Heading
    draw.text((70, 105), scene.get("heading", "Key Concept Recap"), fill=(255, 255, 255), font=fonts["heading"])

    raw_items = scene.get("items", [])
    y = 175
    for idx, item in enumerate(raw_items[:3]):
        val = item.get("value", "") if isinstance(item, dict) else str(item)
        draw.rounded_rectangle([(70, y), (1210, y + 105)], radius=14, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
        # Checkmark Icon
        draw.ellipse([(100, y + 25), (155, y + 80)], fill=(14, 116, 144))
        draw.text((118, y + 36), "✓", fill=(255, 255, 255), font=fonts["heading"])
        # Text
        draw.text((180, y + 36), val, fill=(241, 245, 249), font=fonts["body"])
        y += 125

    draw_caption_bar(draw, scene.get("narration", ""), fonts)
    return img


def render_scene_frame(scene: dict, lesson_title: str, step_str: str) -> Image.Image:
    """Dispatches to appropriate scene renderer."""
    fonts = get_fonts()
    scene_type = scene.get("type", "title_card")
    if scene_type == "code_walkthrough":
        return render_code_card(scene, lesson_title, step_str, fonts)
    elif scene_type == "diagram":
        return render_diagram_card(scene, lesson_title, step_str, fonts)
    elif scene_type == "quiz":
        return render_quiz_card(scene, lesson_title, step_str, fonts)
    elif scene_type == "summary":
        return render_summary_card(scene, lesson_title, step_str, fonts)
    else:
        return render_title_card(scene, lesson_title, step_str, fonts)


def export_lesson_mp4(lesson: dict, output_dir: str) -> tuple[str, float]:
    """
    Renders all frames, encodes scene MP4s with FFmpeg, and concatenates them into final 720p MP4.
    Returns: (final_mp4_path, elapsed_seconds)
    """
    t0 = time.time()
    os.makedirs(output_dir, exist_ok=True)
    scenes = lesson.get("scenes", [])
    total_scenes = len(scenes)
    lesson_title = lesson.get("title", "Blu Visual Lesson")

    scene_mp4_files = []

    for idx, scene in enumerate(scenes):
        step_str = f"Scene {idx + 1} of {total_scenes}"
        img = render_scene_frame(scene, lesson_title, step_str)
        img_path = os.path.join(output_dir, f"frame_{idx}.png")
        img.save(img_path)

        audio_file = scene.get("audio_file")
        if not audio_file:
            audio_file = f"scene_{idx}.wav"
        audio_path = os.path.join(output_dir, audio_file)

        scene_mp4 = f"scene_{idx}.mp4"
        scene_mp4_full = os.path.join(output_dir, scene_mp4)

        # Encode single scene MP4
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", img_path,
            "-i", audio_path,
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            scene_mp4_full
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        scene_mp4_files.append(scene_mp4)

    # Concat all scene MP4s
    list_filename = "concat_list.txt"
    list_path = os.path.join(output_dir, list_filename)
    with open(list_path, "w", encoding="utf-8") as f:
        for fmp4 in scene_mp4_files:
            f.write(f"file '{fmp4}'\n")

    final_mp4_name = "lesson.mp4"
    final_mp4_path = os.path.join(output_dir, final_mp4_name)

    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", list_filename,
        "-c", "copy",
        "-movflags", "+faststart",
        final_mp4_name
    ]
    subprocess.run(concat_cmd, check=True, cwd=output_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    elapsed = time.time() - t0
    logger.info(f"Exported 720p MP4 in {elapsed:.2f}s to {final_mp4_path}")
    return final_mp4_path, elapsed

