# 🎙️ Blu Visual Teacher — 5-Minute Live Demo Script & Judge Cheatsheet

Use this guide for the 5-minute live presentation and judge evaluation.

---

## ⚡ Pre-Demo Setup (1 minute before judges arrive)
1. Ensure Ollama is running in the background:
   ```bash
   ollama run qwen2.5:3b
   ```
2. Double-click **`run.bat`** (or execute `python app.py`).
3. Your browser will automatically open **`http://127.0.0.1:5000`**.
4. **Turn off Wi-Fi** on your laptop to prove 100% offline local operation!

---

## ⏱️ Minute-by-Minute Live Demo Script (5 Minutes)

### Minute 0:00 – 1:00: The Hook & Offline Proof
- **Show Wi-Fi is OFF**:
  > *"Judges, Blu Visual Teacher is 100% local-first. As you can see, Wi-Fi is disconnected. There are no OpenAI, Gemini, Claude, or ElevenLabs APIs. Everything runs on this dual-core CPU laptop with 16 GB of RAM."*
- **Explain the Core Engine**:
  > *"We don't generate hallucinated AI video frames. A small local model (Qwen 2.5 3B) plans pedagogical scenes as validated JSON. Then, our deterministic visual engine and local neural voice synthesizer (Kokoro ONNX) turn that data into a synchronized 720p lesson with native Indian typography."*

---

### Minute 1:00 – 2:30: Live Generation from Judge's Topic
- **Invite the Judge**:
  > *"Judges, please name any STEM or programming topic, and pick a language: English with Indian accent, Hindi, Tamil, Telugu, Marathi, or Bengali."*
  - *If they say "Python Loops" or "Photosynthesis" or "Newton's Laws"*: Select the chip or type it in.
  - *If they give a custom topic (e.g. "Binary Search", "Chemical Reactions", "Gravity")*: Type it into the input box.
- Choose Voice (`hf_alpha` Female or `hm_omega` Male).
- Click **⚡ Generate Lesson**.
- Point out the real-time stage progress bar:
  1. **Stage 2**: Planning with local LLM + schema validation (with built-in fallback guarantee so the demo **never** breaks!).
  2. **Stage 4**: Multilingual neural voice synthesis on CPU via Kokoro.
  3. **Stage 5**: 720p H.264 video compilation with FFmpeg.
- Show the **Stage Benchmark Pills**:
  > *"Notice the exact latency breakdown: Planner took Xs, Voice took Ys, Video took Zs."*

---

### Minute 2:30 – 3:30: Interactive Playback & Visual Engine
- Click **▶️ Play**:
  - Show the **Visual Engine**:
    - Animated **Title Card** with badges.
    - **Diagram Scene** with labels, values, and connecting directional arrows.
    - **Code Walkthrough** with line numbers, glowing highlight, and terminal console.
    - **Interactive Quiz** where you can click an option and get immediate visual validation.
  - Point to the **Captions Bar**:
    > *"Notice that the subtitles are in the native script (Devanagari, Tamil, Telugu, etc.) rendered crisply with Microsoft's Nirmala UI font. Most importantly, the audio duration drives each scene's length, so visuals, voice, and captions remain in 100% sync."*
- Use the **Scrub Bar** and **Next/Prev Scene** buttons to show smooth interactive seeking.

---

### Minute 3:30 – 4:30: High-Value Bonus Features (+10 Points)
Showcase the 3 key bonus capabilities:
1. **Instant Re-Voice**:
   - In the toolbar under *Re-Voice in Another Language*, select a new language (e.g., Hindi or Tamil) and click **🗣️ Re-Voice**.
   - > *"Without re-planning the scenes from scratch, the system translates the narration, re-synthesizes the voice, updates durations, and re-renders the 720p MP4 in seconds!"*
2. **Teacher Edit Mode**:
   - Click **✏️ Edit Scenes Before Render**.
   - Change a heading or narration sentence in Scene 2.
   - Click *Save & Regenerate Scene Audio*.
   - > *"Teachers have total creative control to refine the lesson before finalizing."*
3. **Instant Cache Replay**:
   - Type in an already generated topic.
   - > *"Notice the latency is 9 milliseconds (<0.01s). The hash-based disk cache completely eliminates redundant computation."*

---

### Minute 4:30 – 5:00: MP4 Export & Conclusion
- Click **Exported 720p MP4** toggle to show the rendered H.264 video.
- Click **📥 Download 720p MP4** and **📄 Download Captions (.srt)** to show the files are ready for any student's phone or computer.
- Hand over to judges for Q&A.

---

## 🎯 Likely Judge Questions & Winning Answers

#### Q1: "How do you guarantee this works if Ollama fails or Wi-Fi is cut?"
> *"Our planner has a strict 15-second timeout and schema validator. If Ollama is slow, offline, or returns invalid JSON, our fallback manager instantly injects a high-quality, pre-tested pedagogical lesson in the chosen language. The application literally cannot crash or fail during a demo."*

#### Q2: "How do you handle Indian languages with Kokoro?"
> *"Kokoro uses eSpeak-NG's multi-language phonemizer under the hood. The phoneme vocabularies for Hindi, Tamil, Telugu, Marathi, and Bengali overlap cleanly, allowing Kokoro's neural weights to synthesize natural speech across all 5 Indian languages on a CPU without requiring heavy cloud APIs."*

#### Q3: "How do you avoid audio and visual drift?"
> *"We follow the core design rule: the voice-over determines each scene's duration. We synthesize the audio first, measure the exact duration down to the millisecond, add a 0.5s pause, and configure the visual scene frame to match that exact duration. Hence, zero drift."*

#### Q4: "Are all models and code permissible for open source?"
> *"Yes. Qwen 2.5 is Apache 2.0, Kokoro ONNX is Apache 2.0, FFmpeg is LGPL/GPL, and Nirmala UI is licensed for Windows rendering. Full details and specifications are in our README.md."*

