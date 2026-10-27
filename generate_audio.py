
import asyncio
import edge_tts

TEXT = """
Photosynthesis is how plants make their own food.
Plants use sunlight, water, and carbon dioxide.
Chlorophyll in the leaves captures sunlight.
The plant uses this energy to make glucose and releases oxygen.
Photosynthesis helps plants grow and supports life on Earth.
"""

VOICE = "en-US-AriaNeural"
OUTPUT_FILE = "narration.mp3"


async def main():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Narration saved as {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
