"""
Local Text-to-Speech Engine using Kokoro ONNX.
100% offline, CPU-optimized, supporting Indian-accented English, Hindi, Tamil, Telugu, Marathi, Bengali.
Calculates exact audio durations so scenes and captions stay in perfect sync.
"""

import os
import time
import logging
import numpy as np
import soundfile as sf
import kokoro_onnx

logger = logging.getLogger(__name__)

# Default model paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(BASE_DIR, "models", "voices-v1.0.bin")

# Language to Kokoro phonemizer mapping
LANG_MAP = {
    "en": "en-us",
    "hi": "hi",
    "ta": "ta",
    "te": "te",
    "mr": "mr",
    "bn": "bn"
}

# Voice defaults
VOICE_MAP = {
    "female": "hf_alpha",  # Indian female voice
    "male": "hm_omega"    # Indian male voice
}


class TTSEngine:
    def __init__(self, model_path: str = MODEL_PATH, voices_path: str = VOICES_PATH):
        self.model_path = model_path
        self.voices_path = voices_path
        self._kokoro = None
        self._initialized = False

    def initialize(self):
        if self._initialized:
            return
        if not os.path.exists(self.model_path) or not os.path.exists(self.voices_path):
            raise FileNotFoundError(f"Model or voice file missing: {self.model_path}, {self.voices_path}")
        logger.info("Initializing Kokoro ONNX model...")
        self._kokoro = kokoro_onnx.Kokoro(self.model_path, self.voices_path)
        self._initialized = True
        logger.info("Kokoro ONNX initialized successfully.")

    def synthesize_scene(
        self,
        text: str,
        output_wav_path: str,
        voice: str = "hf_alpha",
        language: str = "en",
        speed: float = 1.0,
        pause_seconds: float = 0.5
    ) -> float:
        """
        Synthesizes speech for a single scene's narration text.
        Appends pause_seconds of silence.
        Returns the total duration in seconds.
        """
        self.initialize()
        lang_code = LANG_MAP.get(language, "en-us")
        
        # Ensure voice name is valid
        if voice in VOICE_MAP:
            voice_id = VOICE_MAP[voice]
        else:
            voice_id = voice if voice in self._kokoro.get_voices() else "hf_alpha"

        try:
            samples, sample_rate = self._kokoro.create(
                text=text,
                voice=voice_id,
                speed=speed,
                lang=lang_code
            )
        except Exception as e:
            logger.warning(f"Kokoro failed for lang '{lang_code}': {e}. Retrying with en-us voice style.")
            try:
                samples, sample_rate = self._kokoro.create(
                    text=text,
                    voice="hf_alpha",
                    speed=speed,
                    lang="en-us"
                )
            except Exception as e2:
                logger.error(f"Fallback TTS failed: {e2}. Generating gentle tone silence.")
                sample_rate = 24000
                samples = np.zeros(sample_rate * 3, dtype=np.float32)

        # Pad with silence at the end so narration does not clip into next scene
        if pause_seconds > 0:
            silence_samples = int(sample_rate * pause_seconds)
            samples = np.concatenate([samples, np.zeros(silence_samples, dtype=samples.dtype)])

        os.makedirs(os.path.dirname(os.path.abspath(output_wav_path)), exist_ok=True)
        sf.write(output_wav_path, samples, sample_rate)
        duration = len(samples) / float(sample_rate)
        return duration

    def synthesize_lesson(
        self,
        lesson: dict,
        output_dir: str,
        voice: str = "hf_alpha",
        speed: float = 1.0,
        pause_seconds: float = 0.5
    ) -> tuple[dict, str, float]:
        """
        Synthesizes audio for all scenes in the lesson.
        Enriches each scene with 'audio_file', 'duration', 'start_time', 'end_time'.
        Generates SubRip (.srt) subtitle string and file.
        Returns: (enriched_lesson, srt_path, total_elapsed_seconds)
        """
        t0 = time.time()
        os.makedirs(output_dir, exist_ok=True)
        current_time = 0.0
        srt_entries = []

        language = lesson.get("language", "en")

        for idx, scene in enumerate(lesson.get("scenes", [])):
            narration = scene.get("narration", "").strip()
            wav_filename = f"scene_{idx}.wav"
            wav_path = os.path.join(output_dir, wav_filename)

            # Generate audio and get exact duration
            dur = self.synthesize_scene(
                text=narration,
                output_wav_path=wav_path,
                voice=voice,
                language=language,
                speed=speed,
                pause_seconds=pause_seconds
            )

            start_time = current_time
            end_time = current_time + dur
            current_time = end_time

            scene["audio_file"] = wav_filename
            scene["duration"] = round(dur, 2)
            scene["start_time"] = round(start_time, 2)
            scene["end_time"] = round(end_time, 2)

            # Build SRT entry
            def format_srt_time(sec: float) -> str:
                hrs = int(sec // 3600)
                mins = int((sec % 3600) // 60)
                s = int(sec % 60)
                ms = int((sec - int(sec)) * 1000)
                return f"{hrs:02d}:{mins:02d}:{s:02d},{ms:03d}"

            srt_entries.append(
                f"{idx + 1}\n{format_srt_time(start_time)} --> {format_srt_time(end_time)}\n{narration}\n"
            )

        lesson["total_duration"] = round(current_time, 2)
        srt_content = "\n".join(srt_entries)
        srt_path = os.path.join(output_dir, "captions.srt")
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(srt_content)

        elapsed = time.time() - t0
        return lesson, srt_path, elapsed


# Global singleton instance
tts_engine = TTSEngine()

