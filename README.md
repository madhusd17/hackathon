# Blu Visual Teacher — Offline Visual Lesson Engine

> **100% Local-First Engine** that turns any typed concept into a short, narrated, animated lesson with synchronized captions and 720p MP4 export in **English and 5 Indian Languages** (Hindi, Tamil, Telugu, Marathi, Bengali).

Built for the **Blu Visual Teacher Hackathon (2026)**.

---

## 🌟 Highlights & Achievements

- **100% Offline & CPU-First**: Runs without internet. No OpenAI, Gemini, Claude, ElevenLabs, or cloud APIs.
- **5 Complete Pipeline Stages**:
  1. **Concept Input**: Web interface for topic, learner level, language, voice, speed, and a 30-second to 5-minute target duration.
  2. **Lesson Planner (Local LLM)**: Local **Qwen 2.5 3B** (via Ollama) generates structured JSON validated against strict JSON Schema, with automatic graceful fallback to curated lessons so live demos never fail.
  3. **Visual Engine**: Reusable animated components for:
     - `title_card` (Animated hero title, concept tags, subtitle)
     - `diagram` (Flowchart with nodes, labels, and connecting arrows)
     - `code_walkthrough` (Visual IDE with line numbers, code highlighting, and execution console)
     - `quiz` (Knowledge check with interactive options and instant feedback)
     - `summary` (Recap checklist)
  4. **Multilingual Narration**: Local neural TTS (**Kokoro ONNX**) on CPU covering Indian-accented English, Hindi, Tamil, Telugu, Marathi, and Bengali with native script captions (Devanagari, Tamil, Telugu, etc.) rendered using Microsoft's `Nirmala UI` universal Indian font. Audio duration dynamically controls scene pacing.
  5. **MP4 Export**: Compiles scenes, audio, and subtitles into downloadable 720p H.264 / AAC video in seconds using FFmpeg.
- **Bonus Features Implemented (+10 Extra Points)**:
  - **6 Languages**: English + 5 Indian languages (Hindi, Tamil, Telugu, Marathi, Bengali).
  - **Re-Voice Lesson**: Switch languages for an already planned lesson without re-planning it.
  - **Voice & Speed Control**: Male (`hm_omega`), Female (`hf_alpha`), and 0.8x–1.3x speed slider.
  - **Adaptive Lesson Planning**: Scene count and narration length scale with the selected video duration; intermediate lessons add a scene when possible, and vocabulary adapts to the learner level.
  - **Teacher Scene Editor**: Tweak narration, code, or headings before rendering and regenerate only that scene.
  - **Lesson Caching**: Hash-based disk cache for instant replay.
  - **Stage Benchmarking**: Live timer display for each stage (Planner, TTS, Video).

---

## 💻 Hardware & Test Environment

- **Laptop Tested**: Intel(R) Core(TM) i7-6600U CPU @ 2.60 GHz (2 Cores, 4 Logical Processors)
- **RAM**: 16 GB RAM (15.89 GB visible)
- **OS**: Windows 10 / 11 (64-bit)
- **GPU**: None (100% CPU inference)
- **Average Generation Time**:
  - LLM Lesson Planning: ~10–25s
  - Kokoro Multilingual TTS: ~3–6s
  - 720p MP4 Video Assembly: ~2–4s
  - Total: ~20–35s (instant <0.05s if cached)

---

## 📜 Models, Voices & Licenses

All models, weights, voices, and assets are open-source and permissible for local offline use:

| Component | Model / Asset | License | Purpose |
| :--- | :--- | :--- | :--- |
| **Lesson Planner** | Qwen 2.5 3B (`qwen2.5:3b`) via Ollama | Apache 2.0 | Local pedagogical lesson structuring |
| **Text-to-Speech** | Kokoro-v1.0 ONNX (`kokoro-onnx`) | Apache 2.0 | CPU neural voice synthesis |
| **Voice Profiles** | `hf_alpha`, `hm_omega`, `hf_beta`, `hm_psi` | Apache 2.0 / CC-BY | Indian-accented English & Indian languages |
| **Indian Typography** | Nirmala UI (`Nirmala.ttf`, `NirmalaB.ttf`) | Microsoft Font License (Built-in Windows) | Native Devanagari, Tamil, Telugu, Bengali scripts |
| **Video Engine** | FFmpeg 9.0.2 Essentials build | LGPL v2.1+ / GPL v2+ | 720p H.264 & AAC encoding |
| **Application Stack** | Python 3.14, Flask, Pillow, Soundfile | BSD / MIT / Apache | Local web server and graphic rendering |

---

## 🚀 Quick Setup & Offline Execution

### 1. Prerequisites (Already bundled or local)
- Python 3.10+ (with `flask`, `pillow`, `soundfile`, `kokoro-onnx`, `jsonschema`, `requests`)
- Ollama running locally with `qwen2.5:3b`:
  ```bash
  ollama run qwen2.5:3b
  ```
- FFmpeg installed and in PATH.

### 2. Start the Application
Run the Flask server:
```bash
python app.py
```
Open your browser at:
```
http://127.0.0.1:5000
```

### 3. Running with Wi-Fi / Internet Switched Off
The application is 100% local-first. Turn off Wi-Fi:
1. Type any topic (or pick a quick chip: "Python Loops", "Photosynthesis", "Newton's 3rd Law").
2. Choose your language: English, Hindi, Tamil, Telugu, Marathi, or Bengali.
3. Click **Generate Lesson**.
4. Play in the interactive engine, toggle to the exported 720p MP4, or download the MP4 and `.srt` captions!

---

## 📁 Repository Structure

```
lesson-to-video/
├── app.py                   # Main Flask offline application
├── core/
│   ├── planner.py           # Ollama client, schema validator, translation
│   ├── fallbacks.py         # Curated multilingual fallback lessons (NEVER breaks)
│   ├── tts_engine.py        # Kokoro ONNX CPU synthesizer & duration calculator
│   ├── video_renderer.py    # Pillow 1280x720 graphic cards & FFmpeg MP4 exporter
│   └── cache_manager.py     # Deterministic caching & instant replay
├── models/
│   ├── kokoro-v1.0.onnx     # Kokoro neural TTS ONNX weights
│   └── voices-v1.0.bin      # Pre-trained voice vectors (54 voices)
├── fonts/
│   ├── Nirmala.ttf          # Regular font for Indian scripts & English
│   └── NirmalaB.ttf         # Bold font for titles & headers
├── static/
│   ├── app.js               # Visual player, scene sync, timeline scrub, editor
│   └── styles.css           # Modern dark-mode responsive styling
├── templates/
│   └── index.html           # Single-page UI
├── output/                  # Generated WAV audio, PNG cards, SRT & MP4 videos
├── cache/                   # Persistent lesson cache
└── README.md                # Project documentation & licenses
```

---

## 🏆 Hackathon Compliance Checklist

- [x] **No external AI APIs**: Zero OpenAI, Gemini, Claude, ElevenLabs, or cloud voice calls.
- [x] **Laptop only**: Tested and benchmarked on a dual-core CPU laptop with 16 GB RAM.
- [x] **Works offline**: Runs with Wi-Fi completely disconnected.
- [x] **Data, not code**: Language model outputs structured JSON only; visuals rendered by custom deterministic components.
- [x] **Light for students**: Responsive web player playable on mobile and desktop browsers.
- [x] **Playable 720p MP4**: Exports 1280x720 H.264 video with AAC audio and matching subtitles.
- [x] **Audio sets scene duration**: Visuals and audio stay in step with no drift.
- [x] **Fallback robustness**: Bad LLM responses or timeouts fall back instantly to built-in lessons.
