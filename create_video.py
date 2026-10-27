
import subprocess

command = [
    "ffmpeg",
    "-y",
    "-f", "lavfi",
    "-i", "color=c=darkgreen:s=1280x720:r=25:d=25",
    "-i", "narration.mp3",
    "-vf",
    "drawtext=text='PHOTOSYNTHESIS':"
    "fontcolor=white:fontsize=54:"
    "x=(w-text_w)/2:y=(h-text_h)/2-40,"
    "drawtext=text='How plants make their food':"
    "fontcolor=yellow:fontsize=30:"
    "x=(w-text_w)/2:y=(h-text_h)/2+40",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    "photosynthesis.mp4"
]

subprocess.run(command, check=True)
print("Video created: photosynthesis.mp4")
