/**
 * Blu Visual Teacher — Client Controller
 * Manages Lesson Generation, Interactive Player, Synced Narration, Captions, Revoicing, and Editing.
 */

let currentLesson = null;
let currentFolder = "";
let currentSceneIdx = 0;
let isPlaying = false;
let editingSceneIdx = 0;
let sceneTimer = null;

const audioPlayer = document.getElementById("scene-audio");

function setTopic(val) {
  document.getElementById("topic-input").value = val;
}

function updateDurationLabel(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  document.getElementById("duration-val").innerText =
    `${minutes}:${String(remainingSeconds).padStart(2, "0")}`;
}

// ----------------------------------------------------
// 1. GENERATE LESSON (Stage 1 & 2 -> 3, 4, 5)
// ----------------------------------------------------
async function generateLesson() {
  const topic = document.getElementById("topic-input").value.trim();
  const lang = document.getElementById("lang-select").value;
  const voice = document.getElementById("voice-select").value;
  const level = document.getElementById("level-select").value;
  const speed = parseFloat(document.getElementById("speed-slider").value);
  const targetLength = parseInt(document.getElementById("duration-slider").value, 10);
  const forceRefresh = document.getElementById("force-refresh").checked;

  if (!topic) return;

  currentLesson = null;
  audioPlayer.pause();
  document.getElementById("mp4-video").pause();
  document.getElementById("player-section").classList.add("hidden");

  // Show status indicator
  const statusCard = document.getElementById("generation-status");
  const statusTitle = document.getElementById("status-title");
  const statusDesc = document.getElementById("status-desc");
  const progressFill = document.getElementById("progress-bar-fill");
  const generateBtn = document.getElementById("generate-btn");

  statusCard.classList.remove("hidden");
  generateBtn.disabled = true;
  document.getElementById("btn-text").innerText = "Generating...";

  // Progress simulation steps
  statusTitle.innerText = "Stage 2: Planning Lesson...";
  statusDesc.innerText = "Local Ollama LLM (Qwen 2.5 3B) is designing structured pedagogical scenes...";
  progressFill.style.width = "30%";

  const ttsTimeout = setTimeout(() => {
    statusTitle.innerText = "Stage 4: Synthesizing Multilingual Speech...";
    statusDesc.innerText = "Local Kokoro ONNX is generating natural voice-over & calculating scene durations...";
    progressFill.style.width = "65%";
  }, 3000);

  const videoTimeout = setTimeout(() => {
    statusTitle.innerText = "Stage 5: Rendering 720p H.264 MP4...";
    statusDesc.innerText = "FFmpeg and Canvas engine are drawing graphic scenes and compiling video...";
    progressFill.style.width = "85%";
  }, 7000);

  try {
    const res = await fetch("/api/generate_full_lesson", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        topic: topic,
        language: lang,
        voice: voice,
        level: level,
        speed: speed,
        target_length: targetLength,
        force_refresh: forceRefresh
      })
    });

    clearTimeout(ttsTimeout);
    clearTimeout(videoTimeout);

    const contentType = res.headers.get("content-type") || "";
    if (!contentType.includes("application/json")) {
      throw new Error(`The server returned an unexpected response (HTTP ${res.status}) instead of JSON. Check the server logs.`);
    }

    const data = await res.json();
    if (!data.success) {
      alert("Generation error: " + (data.error || "Unknown error"));
      return;
    }
    const requestedTopic = topic.replace(/\s+/g, " ").toLocaleLowerCase();
    const returnedTopic = String(data.lesson?.topic || "").replace(/\s+/g, " ").toLocaleLowerCase();
    if (returnedTopic !== requestedTopic) {
      throw new Error("The server returned a lesson for a different topic. Please generate it again.");
    }

    progressFill.style.width = "100%";
    statusTitle.innerText = "Complete!";
    statusDesc.innerText = "Lesson is ready for playback and export.";

    setTimeout(() => {
      statusCard.classList.add("hidden");
    }, 1000);

    // Update state
    currentLesson = data.lesson;
    currentFolder = data.folder;

    // Display metrics
    displayMetrics(data.metrics, data.cached);

    // Load into player
    loadLessonIntoPlayer(currentLesson, currentFolder);

    // Refresh cached list
    loadCachedLessons();

  } catch (err) {
    clearTimeout(ttsTimeout);
    clearTimeout(videoTimeout);
    alert("Generation failed: " + err.message);
  } finally {
    generateBtn.disabled = false;
    document.getElementById("btn-text").innerText = "Generate Lesson";
  }
}

// ----------------------------------------------------
// 2. METRICS DISPLAY
// ----------------------------------------------------
function displayMetrics(metrics, isCached) {
  const bar = document.getElementById("metrics-bar");
  bar.classList.remove("hidden");
  document.getElementById("m-planner").innerText = `${metrics.planner_s}s`;
  document.getElementById("m-tts").innerText = `${metrics.tts_s}s`;
  document.getElementById("m-video").innerText = `${metrics.video_s}s`;
  document.getElementById("m-total").innerText = `${metrics.total_s}s`;

  const cachedBadge = document.getElementById("cached-badge");
  if (isCached) {
    cachedBadge.classList.remove("hidden");
  } else {
    cachedBadge.classList.add("hidden");
  }

  const fallbackBadge = document.getElementById("fallback-badge");
  fallbackBadge.classList.toggle("hidden", !metrics.used_fallback);

  const translationWarningBadge = document.getElementById("translation-warning-badge");
  translationWarningBadge.innerText = metrics.translation_warning || "";
  translationWarningBadge.classList.toggle("hidden", !metrics.translation_warning);
}

// ----------------------------------------------------
// 3. LOAD LESSON INTO PLAYER
// ----------------------------------------------------
function loadLessonIntoPlayer(lesson, folder) {
  const section = document.getElementById("player-section");
  section.classList.remove("hidden");

  document.getElementById("lesson-display-title").innerText = lesson.title || "Visual Lesson";
  const langNames = { en: "English", hi: "Hindi", ta: "Tamil", te: "Telugu", mr: "Marathi", bn: "Bengali" };
  const langLabel = langNames[lesson.language] || lesson.language.toUpperCase();
  const actualDuration = formatDuration(lesson.total_duration || 0);
  const targetDuration = formatDuration(lesson.target_duration || lesson.total_duration || 0);
  document.getElementById("lesson-sub-meta").innerText =
    `${lesson.level || "Beginner"} • ${langLabel} • ${lesson.scenes.length} Scenes • ${actualDuration} / ${targetDuration} target`;

  // Set MP4 source
  const mp4Video = document.getElementById("mp4-video");
  const mp4Source = document.getElementById("mp4-source");
  const mp4Url = `/media/${folder}/lesson.mp4?t=${Date.now()}`;
  if (mp4Source) mp4Source.src = mp4Url;
  mp4Video.src = mp4Url;
  mp4Video.muted = false;
  mp4Video.volume = 1.0;
  mp4Video.load();

  // Set Download Links
  document.getElementById("download-mp4-btn").href = `/api/download/${folder}/lesson.mp4`;
  document.getElementById("download-srt-btn").href = `/api/download/${folder}/captions.srt`;

  // Create scrub markers
  createScrubMarkers(lesson.scenes, lesson.total_duration);

  // Initialize Scene 0
  currentSceneIdx = 0;
  renderScene(0);

  // Scroll to player
  section.scrollIntoView({ behavior: "smooth", block: "start" });
}

function createScrubMarkers(scenes, totalDur) {
  const markersContainer = document.getElementById("scene-markers");
  markersContainer.innerHTML = "";
  if (!totalDur || totalDur <= 0) return;

  scenes.forEach((sc, idx) => {
    if (idx > 0) {
      const pct = (sc.start_time / totalDur) * 100;
      const marker = document.createElement("div");
      marker.className = "scene-marker";
      marker.style.left = `${pct}%`;
      marker.title = `Scene ${idx + 1}: ${sc.heading}`;
      markersContainer.appendChild(marker);
    }
  });
}

function formatDuration(seconds) {
  const mins = Math.floor(seconds / 60);
  const remaining = Math.floor(seconds % 60);
  return `${mins}:${String(remaining).padStart(2, "0")}`;
}

// ----------------------------------------------------
// 4. SCENE RENDERING ENGINE (Stage 3 & 4)
// ----------------------------------------------------
function renderScene(idx) {
  if (!currentLesson || !currentLesson.scenes || idx >= currentLesson.scenes.length) return;
  currentSceneIdx = idx;
  const scene = currentLesson.scenes[idx];
  const container = document.getElementById("scene-container");

  // Update Topbar
  document.getElementById("stage-topic-badge").innerText = currentLesson.title;
  document.getElementById("stage-step-badge").innerText = `Scene ${idx + 1} of ${currentLesson.scenes.length}`;

  // Update Caption
  document.getElementById("caption-text").innerText = scene.narration || "";

  // Render Component by Type
  const type = scene.type || "title_card";

  if (type === "title_card") {
    container.innerHTML = `
      <div class="scene-title-card">
        <span class="concept-tag">CONCEPT INTRODUCTION</span>
        <h2>${escapeHtml(scene.heading)}</h2>
        <p>${escapeHtml(scene.subheading || "")}</p>
        <div class="icon-bulb">💡</div>
      </div>
    `;
  } else if (type === "diagram") {
    const rawItems = scene.items || [];
    let nodesHtml = "";
    rawItems.forEach((it, i) => {
      let label = "Step " + (i + 1);
      let val = "";
      if (typeof it === "object" && it !== null) {
        label = it.label || label;
        val = it.value || "";
      } else if (typeof it === "string") {
        const parts = it.split(":");
        if (parts.length === 2) {
          label = parts[0];
          val = parts[1];
        } else {
          val = it;
        }
      }
      nodesHtml += `
        <div class="diagram-node ${i === 0 ? 'active-node' : ''}">
          <span class="step-badge">${escapeHtml(label)}</span>
          <div class="node-value">${escapeHtml(val)}</div>
        </div>
      `;
      if (i < rawItems.length - 1) {
        nodesHtml += `<div class="arrow-connector">➔</div>`;
      }
    });

    container.innerHTML = `
      <h3 style="font-size: 22px; color: #fff; margin-bottom: 8px;">${escapeHtml(scene.heading)}</h3>
      <div class="diagram-grid">
        ${nodesHtml}
      </div>
    `;
  } else if (type === "code_walkthrough") {
    const code = scene.code || "for i in range(3):\n    print(i)";
    const lines = code.split("\n");
    const highlightLines = scene.highlight_lines || [1];

    let codeLinesHtml = "";
    lines.forEach((l, lIdx) => {
      const lineNum = lIdx + 1;
      const isHl = highlightLines.includes(lineNum);
      codeLinesHtml += `
        <div class="code-line ${isHl ? 'highlight' : ''}">
          <span class="line-no">${lineNum}</span>
          <span>${escapeHtml(l)}</span>
        </div>
      `;
    });

    let outputHtml = "";
    if (scene.output) {
      outputHtml = `
        <div class="terminal-box">
          <span style="color: #64748b; font-size: 11px;">OUTPUT CONSOLE:</span><br>
          ${escapeHtml(scene.output).replace(/\n/g, '<br>')}
        </div>
      `;
    }

    container.innerHTML = `
      <h3 style="font-size: 22px; color: #fff; margin-bottom: 8px;">${escapeHtml(scene.heading)}</h3>
      <div class="ide-window">
        <div class="ide-header">
          <span class="dot-btn dot-red"></span>
          <span class="dot-btn dot-yellow"></span>
          <span class="dot-btn dot-green"></span>
          <span class="ide-title">main.py — Visual Execution</span>
        </div>
        <div class="code-editor">
          ${codeLinesHtml}
        </div>
        ${outputHtml}
      </div>
    `;
  } else if (type === "quiz") {
    const opts = scene.options || ["A", "B", "C", "D"];
    const ans = scene.answer || "";
    let optsHtml = "";
    opts.forEach((o, oIdx) => {
      const label = ["A", "B", "C", "D"][oIdx] || "";
      const isCorrect = String(o).trim() === String(ans).trim();
      optsHtml += `
        <div class="quiz-option ${isCorrect ? 'correct' : ''}" onclick="selectQuizOption(this, ${isCorrect})">
          <span style="font-weight: bold; color: var(--color-purple);">${label}.</span>
          <span>${escapeHtml(String(o))}</span>
          ${isCorrect ? '<span style="margin-left: auto;">✓</span>' : ''}
        </div>
      `;
    });

    container.innerHTML = `
      <div class="quiz-container">
        <h3 style="font-size: 20px; color: #fff;">${escapeHtml(scene.heading)}</h3>
        <div class="quiz-question">❓ ${escapeHtml(scene.question || "Knowledge Check")}</div>
        <div class="quiz-grid">
          ${optsHtml}
        </div>
      </div>
    `;
  } else if (type === "summary") {
    const items = scene.items || [];
    let itemsHtml = "";
    items.forEach(it => {
      const val = typeof it === "object" ? it.value : it;
      itemsHtml += `
        <div class="summary-item">
          <div class="summary-check">✓</div>
          <div>${escapeHtml(val)}</div>
        </div>
      `;
    });

    container.innerHTML = `
      <h3 style="font-size: 22px; color: #fff; margin-bottom: 12px;">${escapeHtml(scene.heading)}</h3>
      <div class="summary-list">
        ${itemsHtml}
      </div>
    `;
  }

  // Load Audio for this scene
  const audioFile = scene.audio_file || `scene_${idx}.wav`;
  audioPlayer.src = `/media/${currentFolder}/${audioFile}?t=${Date.now()}`;
  audioPlayer.volume = 1.0;

  updateTimeDisplay();
}

function selectQuizOption(elem, isCorrect) {
  if (isCorrect) {
    elem.style.transform = "scale(1.03)";
  } else {
    elem.style.borderColor = "#ef4444";
    elem.style.background = "rgba(239, 68, 68, 0.2)";
  }
}

// ----------------------------------------------------
// 5. SYNCHRONIZED PLAYBACK CONTROLS
// ----------------------------------------------------
function togglePlayPause() {
  if (isPlaying) {
    pause();
  } else {
    play();
  }
}

function play() {
  if (!currentLesson) return;
  isPlaying = true;
  document.getElementById("play-pause-btn").innerText = "⏸ Pause";

  audioPlayer.play().catch(e => console.log("Audio play error:", e));
}

function pause() {
  isPlaying = false;
  document.getElementById("play-pause-btn").innerText = "▶️ Play";
  audioPlayer.pause();
}

audioPlayer.onended = function () {
  // When scene audio completes, move seamlessly to next scene!
  if (currentSceneIdx < currentLesson.scenes.length - 1) {
    renderScene(currentSceneIdx + 1);
    if (isPlaying) {
      audioPlayer.play().catch(e => console.log(e));
    }
  } else {
    // End of lesson
    pause();
  }
};

audioPlayer.ontimeupdate = function () {
  updateTimeDisplay();
};

function updateTimeDisplay() {
  if (!currentLesson) return;
  const scenes = currentLesson.scenes;
  const currentScene = scenes[currentSceneIdx];
  if (!currentScene) return;

  const sceneStart = currentScene.start_time || 0;
  const currentTotalTime = sceneStart + audioPlayer.currentTime;
  const totalDuration = currentLesson.total_duration || 1;

  // Format MM:SS
  const fmt = (s) => {
    const mins = Math.floor(s / 60);
    const secs = Math.floor(s % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  document.getElementById("time-display").innerText = `${fmt(currentTotalTime)} / ${fmt(totalDuration)}`;

  // Progress scrub fill
  const pct = Math.min(100, (currentTotalTime / totalDuration) * 100);
  document.getElementById("scrub-fill").style.width = `${pct}%`;

  // Dynamic step node highlighting for diagrams
  if (currentScene && currentScene.type === "diagram") {
    const nodes = document.querySelectorAll(".diagram-node");
    if (nodes.length > 0) {
      const sceneDur = currentScene.duration || 1;
      const progress = Math.min(0.99, audioPlayer.currentTime / sceneDur);
      const activeIdx = Math.floor(progress * nodes.length);
      nodes.forEach((n, idx) => {
        n.classList.toggle("active-node", idx === activeIdx);
      });
    }
  }
}

function prevScene() {
  if (currentSceneIdx > 0) {
    renderScene(currentSceneIdx - 1);
    if (isPlaying) audioPlayer.play();
  }
}

function nextScene() {
  if (currentLesson && currentSceneIdx < currentLesson.scenes.length - 1) {
    renderScene(currentSceneIdx + 1);
    if (isPlaying) audioPlayer.play();
  }
}

function replayLesson() {
  renderScene(0);
  play();
}

function handleScrub(e) {
  if (!currentLesson || !currentLesson.total_duration) return;
  const rect = e.currentTarget.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const pct = clickX / rect.width;
  const targetTime = pct * currentLesson.total_duration;

  // Find target scene
  const scenes = currentLesson.scenes;
  for (let i = 0; i < scenes.length; i++) {
    if (targetTime >= scenes[i].start_time && targetTime <= scenes[i].end_time) {
      renderScene(i);
      audioPlayer.currentTime = targetTime - scenes[i].start_time;
      if (isPlaying) audioPlayer.play();
      break;
    }
  }
}

function switchView(mode) {
  const interactiveStage = document.getElementById("interactive-stage");
  const mp4Stage = document.getElementById("mp4-stage");
  const btnInteractive = document.getElementById("btn-view-interactive");
  const btnMp4 = document.getElementById("btn-view-mp4");
  const mp4Video = document.getElementById("mp4-video");

  if (mode === "interactive") {
    interactiveStage.classList.remove("hidden");
    mp4Stage.classList.add("hidden");
    btnInteractive.classList.add("active");
    btnMp4.classList.remove("active");
    mp4Video.pause();
  } else {
    interactiveStage.classList.add("hidden");
    mp4Stage.classList.remove("hidden");
    btnInteractive.classList.remove("active");
    btnMp4.classList.add("active");
    pause(); // pause interactive audio
    mp4Video.muted = false;
    mp4Video.volume = 1.0;
    mp4Video.play().catch(e => console.log(e));
  }
}

// ----------------------------------------------------
// 6. BONUS FEATURE: RE-VOICE LESSON (Without re-planning)
// ----------------------------------------------------
async function revoiceCurrentLesson() {
  if (!currentLesson) return;
  const newLang = document.getElementById("revoice-lang-select").value;
  const voice = document.getElementById("voice-select").value;
  const speed = parseFloat(document.getElementById("speed-slider").value);

  const statusCard = document.getElementById("generation-status");
  const statusTitle = document.getElementById("status-title");
  const statusDesc = document.getElementById("status-desc");
  const progressFill = document.getElementById("progress-bar-fill");

  statusCard.classList.remove("hidden");
  statusTitle.innerText = "Re-voicing Lesson Plan...";
  statusDesc.innerText = `Synthesizing audio and rebuilding subtitles in ${newLang.toUpperCase()} without re-planning...`;
  progressFill.style.width = "50%";

  try {
    const res = await fetch("/api/revoice", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        lesson: currentLesson,
        new_language: newLang,
        new_voice: voice,
        speed: speed
      })
    });

    const data = await res.json();
    if (!data.success) {
      alert("Revoice error: " + (data.error || "Failed"));
      return;
    }

    progressFill.style.width = "100%";
    statusTitle.innerText = "Re-voicing Complete!";
    statusDesc.innerText = "Playing in new language...";
    setTimeout(() => statusCard.classList.add("hidden"), 1000);

    currentLesson = data.lesson;
    currentFolder = data.folder;
    displayMetrics(data.metrics, false);
    loadLessonIntoPlayer(currentLesson, currentFolder);
    play();

  } catch (err) {
    alert("Revoice error: " + err.message);
  }
}

// ----------------------------------------------------
// 7. BONUS FEATURE: TEACHER SCENE EDITOR
// ----------------------------------------------------
function openTeacherEditor() {
  if (!currentLesson) return;
  const modal = document.getElementById("edit-modal");
  modal.classList.remove("hidden");

  // Build Scene tabs
  const tabsContainer = document.getElementById("edit-scene-tabs");
  tabsContainer.innerHTML = "";
  currentLesson.scenes.forEach((sc, i) => {
    const tab = document.createElement("button");
    tab.className = `scene-tab ${i === currentSceneIdx ? 'active' : ''}`;
    tab.innerText = `Scene ${i + 1}`;
    tab.onclick = () => selectEditScene(i);
    tabsContainer.appendChild(tab);
  });

  selectEditScene(currentSceneIdx);
}

function selectEditScene(idx) {
  editingSceneIdx = idx;
  const tabs = document.querySelectorAll(".scene-tab");
  tabs.forEach((t, i) => t.classList.toggle("active", i === idx));

  const scene = currentLesson.scenes[idx];
  document.getElementById("edit-heading").value = scene.heading || "";
  document.getElementById("edit-narration").value = scene.narration || "";

  const codeGroup = document.getElementById("edit-code-group");
  if (scene.code !== undefined) {
    codeGroup.style.display = "block";
    document.getElementById("edit-code").value = scene.code;
  } else {
    codeGroup.style.display = "none";
  }
}

async function saveAndRegenerateScene() {
  if (!currentLesson) return;
  const scene = currentLesson.scenes[editingSceneIdx];
  scene.heading = document.getElementById("edit-heading").value;
  scene.narration = document.getElementById("edit-narration").value;
  if (scene.code !== undefined) {
    scene.code = document.getElementById("edit-code").value;
  }

  closeTeacherEditor();

  // Call edit scene endpoint
  try {
    const res = await fetch("/api/edit_scene", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        lesson: currentLesson,
        scene_index: editingSceneIdx,
        updated_scene: scene
      })
    });
    const data = await res.json();
    if (data.success) {
      currentLesson = data.lesson;
      currentFolder = data.folder;
      loadLessonIntoPlayer(currentLesson, currentFolder);
      renderScene(editingSceneIdx);
    }
  } catch (err) {
    alert("Error updating scene: " + err.message);
  }
}

function closeTeacherEditor() {
  document.getElementById("edit-modal").classList.add("hidden");
}

// ----------------------------------------------------
// 8. BONUS FEATURE: CACHE LIBRARY LIST
// ----------------------------------------------------
async function loadCachedLessons() {
  try {
    const res = await fetch("/api/cached_lessons");
    const data = await res.json();
    const container = document.getElementById("cache-list");
    if (!data.lessons || data.lessons.length === 0) {
      container.innerHTML = '<p class="placeholder-text">No cached lessons yet. Generate one above!</p>';
      return;
    }

    container.innerHTML = "";
    data.lessons.forEach(l => {
      const card = document.createElement("div");
      card.className = "cache-item";
      card.innerHTML = `
        <h4>${escapeHtml(l.title)}</h4>
        <p>Topic: ${escapeHtml(l.topic)} • ${l.language.toUpperCase()} • ${l.scenes_count} scenes (${l.total_duration}s)</p>
      `;
      card.onclick = () => loadCachedItem(l.cache_key);
      container.appendChild(card);
    });
  } catch (e) {
    console.log("Could not load cache:", e);
  }
}

async function loadCachedItem(cacheKey) {
  try {
    const res = await fetch(`/api/load_cache/${cacheKey}`);
    const data = await res.json();
    if (data.success) {
      currentLesson = data.lesson;
      currentFolder = data.folder;
      displayMetrics(data.metrics, true);
      loadLessonIntoPlayer(currentLesson, currentFolder);
      play();
    }
  } catch (err) {
    console.error("Error loading cached lesson:", err);
  }
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// Load cache list on start
window.addEventListener("DOMContentLoaded", () => {
  loadCachedLessons();
});
