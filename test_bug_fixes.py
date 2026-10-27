import hashlib
import json
import os
import tempfile
import unittest
from unittest.mock import Mock, patch

import numpy as np
import soundfile as sf

from core.cache_manager import get_cache_key


class CacheKeyTests(unittest.TestCase):
    def test_cache_keys_use_presentation_generation_version(self):
        raw = "photosynthesis_hi_beginner_hf_alpha_duration_calibrated_v3"
        expected = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]

        self.assertEqual(
            get_cache_key("Photosynthesis", "hi", "beginner"),
            expected,
        )

    def test_speech_speed_and_target_length_have_distinct_cache_keys(self):
        base = get_cache_key("Photosynthesis", "hi", "beginner")

        self.assertNotEqual(
            base,
            get_cache_key("Photosynthesis", "hi", "beginner", speed=1.2),
        )
        self.assertNotEqual(
            base,
            get_cache_key("Photosynthesis", "hi", "beginner", target_length=30),
        )
        self.assertEqual(
            get_cache_key("Photosynthesis", "hi", "beginner", speed=1.2),
            get_cache_key("Photosynthesis", "hi", "beginner", speed=1.2),
        )


class LessonPlannerTests(unittest.TestCase):
    def test_long_scene_translation_has_room_for_full_narration(self):
        from core.planner import translate_lesson_plan

        response = Mock()
        response.status_code = 200
        response.json.return_value = {"response": json.dumps(["अनुवादित पाठ"], ensure_ascii=False)}
        plan = {
            "title": "A lesson",
            "level": "beginner",
            "language": "en",
            "scenes": [
                {
                    "type": "diagram",
                    "heading": "A detailed slide",
                    "narration": " ".join(["explanation"] * 100),
                }
            ],
        }

        with patch("core.planner.requests.post", return_value=response) as post:
            translated = translate_lesson_plan(plan, "hi")

        self.assertEqual(translated["scenes"][0]["narration"], "अनुवादित पाठ")
        self.assertEqual(post.call_args.kwargs["json"]["options"]["num_predict"], 500)
        self.assertEqual(post.call_args.kwargs["timeout"], 20)
        self.assertIn("same order", post.call_args.kwargs["json"]["prompt"])

    def test_translation_failure_preserves_generated_lesson(self):
        from core.planner import translate_lesson_plan
        import requests

        plan = {
            "title": "Photosynthesis: A Custom Lesson",
            "topic": "Photosynthesis",
            "level": "intermediate",
            "language": "en",
            "scenes": [
                {"type": "title_card", "heading": "Light to Food", "narration": "A custom explanation."},
                {"type": "summary", "heading": "Recap", "narration": "A custom recap."},
            ],
        }

        with patch("core.planner.requests.post", side_effect=requests.ConnectionError):
            translated = translate_lesson_plan(plan, "hi")

        self.assertEqual(translated["title"], "Photosynthesis: A Custom Lesson")
        self.assertEqual(translated["language"], "en")
        self.assertIn("translation_warning", translated)

    def test_local_model_is_tried_before_curated_fallback(self):
        from core.planner import generate_lesson_plan

        model_plan = {
            "title": "Photosynthesis: A Custom Lesson",
            "level": "intermediate",
            "language": "en",
            "scenes": [
                {
                    "type": "title_card" if i == 0 else "summary" if i == 10 else "diagram",
                    "heading": f"Photosynthesis slide {i + 1}",
                    "narration": f"Topic-specific explanation for slide {i + 1}.",
                    "items": [{"label": "Key idea", "value": f"Slide detail {i + 1}"}],
                }
                for i in range(11)
            ],
        }
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"response": json.dumps(model_plan)}

        with (
            patch("core.planner.requests.post", return_value=response) as post,
            patch("core.planner.translate_lesson_plan", side_effect=lambda plan, language: plan),
        ):
            plan, used_fallback, _ = generate_lesson_plan(
                "Photosynthesis", level="intermediate", target_length=300, speed=1.2
            )

        self.assertFalse(used_fallback)
        self.assertEqual(plan["title"], "Photosynthesis: A Custom Lesson")
        self.assertEqual(len(plan["scenes"]), 11)
        prompt = post.call_args.kwargs["json"]["prompt"]
        self.assertIn("Learner level: intermediate", prompt)
        self.assertIn("Target video duration: 300 seconds", prompt)
        self.assertIn("Narration speed: 1.2x", prompt)
        self.assertIn("Create exactly 11 presentation slides (scenes)", prompt)
        self.assertIn("about 1060 spoken words", prompt)
        self.assertIn("appropriate technical vocabulary", prompt)
        self.assertIn("Do not fill the extra slides by repeating generic summaries", prompt)
        self.assertEqual(post.call_args.kwargs["json"]["options"]["num_predict"], 2400)
        schema = post.call_args.kwargs["json"]["format"]
        self.assertEqual(schema["properties"]["scenes"]["minItems"], 11)
        self.assertEqual(schema["properties"]["scenes"]["maxItems"], 11)

    def test_short_duration_requests_three_slides_and_beginner_language(self):
        from core.planner import generate_lesson_plan

        model_plan = {
            "title": "A Lesson",
            "level": "beginner",
            "language": "en",
            "scenes": [
                {"type": "title_card", "heading": "Intro", "narration": "Start simply."},
                {"type": "diagram", "heading": "Example", "narration": "Explain simply.", "items": [
                    {"label": "Example", "value": "A familiar example."}
                ]},
                {"type": "summary", "heading": "Recap", "narration": "Finish simply."},
            ],
        }
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"response": json.dumps(model_plan)}

        with (
            patch("core.planner.requests.post", return_value=response) as post,
            patch("core.planner.translate_lesson_plan", side_effect=lambda plan, language: plan),
        ):
            generate_lesson_plan("Fractions", level="beginner", target_length=30)

        prompt = post.call_args.kwargs["json"]["prompt"]
        self.assertIn("Target video duration: 30 seconds", prompt)
        self.assertIn("Create exactly 3 presentation slides (scenes)", prompt)
        self.assertIn("use everyday words", prompt)

    def test_intermediate_level_adds_a_scene_at_short_duration(self):
        from core.planner import generate_lesson_plan

        model_plan = {
            "title": "A Lesson",
            "level": "intermediate",
            "language": "en",
            "scenes": [
                {"type": "title_card", "heading": "Intro", "narration": "Introduce the topic."},
                {"type": "diagram", "heading": "Example", "narration": "Use a topic example.", "items": [
                    {"label": "Example", "value": "A distinct example."}
                ]},
                {"type": "diagram", "heading": "Explain", "narration": "Explain the topic.", "items": [
                    {"label": "Key idea", "value": "A distinct topic concept."}
                ]},
                {"type": "summary", "heading": "Recap", "narration": "Recap the topic."},
            ],
        }
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"response": json.dumps(model_plan)}

        with (
            patch("core.planner.requests.post", return_value=response) as post,
            patch("core.planner.translate_lesson_plan", side_effect=lambda plan, language: plan),
        ):
            generate_lesson_plan("Fractions", level="intermediate", target_length=30)

        self.assertIn("Create exactly 4 presentation slides (scenes)", post.call_args.kwargs["json"]["prompt"])

    def test_slide_schema_allows_longer_presentations(self):
        from core.planner import LESSON_SCHEMA

        self.assertEqual(LESSON_SCHEMA["properties"]["scenes"]["minItems"], 3)
        self.assertEqual(LESSON_SCHEMA["properties"]["scenes"]["maxItems"], 12)


class LessonDurationTests(unittest.TestCase):
    def test_tts_pads_final_scene_to_requested_video_duration(self):
        from core.tts_engine import TTSEngine

        lesson = {
            "language": "en",
            "scenes": [
                {"type": "title_card", "heading": "Intro", "narration": "Introduction."},
                {"type": "summary", "heading": "Recap", "narration": "Recap."},
            ],
        }

        with tempfile.TemporaryDirectory() as output_dir:
            engine = TTSEngine()

            def write_two_second_audio(text, output_wav_path, **kwargs):
                sf.write(output_wav_path, np.zeros(48000, dtype=np.float32), 24000)
                return 2.0

            with patch.object(engine, "synthesize_scene", side_effect=write_two_second_audio):
                enriched, _, _ = engine.synthesize_lesson(
                    lesson,
                    output_dir,
                    target_duration=10,
                )

            last_scene_path = os.path.join(output_dir, enriched["scenes"][-1]["audio_file"])
            samples, sample_rate = sf.read(last_scene_path)

        self.assertEqual(sample_rate, 24000)
        self.assertEqual(len(samples), 8 * sample_rate)
        self.assertEqual(enriched["total_duration"], 10)
        self.assertEqual(enriched["scenes"][-1]["end_time"], 10)

    def test_tts_never_cuts_audio_longer_than_requested_duration(self):
        from core.tts_engine import TTSEngine

        lesson = {
            "language": "en",
            "scenes": [
                {"type": "summary", "heading": "Recap", "narration": "Recap."},
            ],
        }

        with tempfile.TemporaryDirectory() as output_dir:
            engine = TTSEngine()

            def write_two_second_audio(text, output_wav_path, **kwargs):
                sf.write(output_wav_path, np.zeros(48000, dtype=np.float32), 24000)
                return 2.0

            with patch.object(engine, "synthesize_scene", side_effect=write_two_second_audio):
                enriched, _, _ = engine.synthesize_lesson(
                    lesson,
                    output_dir,
                    target_duration=1,
                )

        self.assertEqual(enriched["total_duration"], 2)


class EditSceneValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import app

        cls.app_module = app

    def setUp(self):
        self.client = self.app_module.app.test_client()

    def test_rejects_missing_lesson_without_server_error(self):
        response = self.client.post("/api/edit_scene", json={"updated_scene": {}})

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["success"])

    def test_rejects_non_object_request_body(self):
        response = self.client.post("/api/edit_scene", json=[])

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["success"])

    def test_rejects_negative_scene_index_without_editing_last_scene(self):
        response = self.client.post(
            "/api/edit_scene",
            json={
                "lesson": {"scenes": [{"duration": 1.0}]},
                "scene_index": -1,
                "updated_scene": {"narration": "Changed"},
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["success"])

    def test_rejects_non_integer_scene_index(self):
        response = self.client.post(
            "/api/edit_scene",
            json={
                "lesson": {"scenes": [{"duration": 1.0}]},
                "scene_index": "invalid",
                "updated_scene": {"narration": "Changed"},
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["success"])

    def test_generation_includes_speed_and_length_in_cache_lookup(self):
        with (
            patch.object(self.app_module, "get_cache_key", return_value="cache-key") as key_builder,
            patch.object(self.app_module, "get_cached_lesson", return_value={"scenes": []}),
        ):
            response = self.client.post(
                "/api/generate_full_lesson",
                json={
                    "topic": "Photosynthesis",
                    "language": "hi",
                    "level": "beginner",
                    "speed": 1.2,
                    "target_length": 30,
                },
            )

        self.assertEqual(response.status_code, 200)
        key_builder.assert_called_once_with(
            "Photosynthesis", "hi", "beginner", "hf_alpha", 1.2, 30
        )

    def test_generation_rejects_duration_outside_supported_range(self):
        response = self.client.post(
            "/api/generate_full_lesson",
            json={"topic": "Photosynthesis", "target_length": 301},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("30 and 300 seconds", response.get_json()["error"])

    def test_generation_pipeline_errors_are_returned_as_json(self):
        with (
            patch.object(
                self.app_module,
                "get_cache_key",
                return_value="uncached-key",
            ),
            patch.object(self.app_module, "get_cached_lesson", return_value=None),
            patch.object(
                self.app_module,
                "generate_lesson_plan",
                return_value=(
                    {
                        "title": "A lesson",
                        "level": "beginner",
                        "language": "en",
                        "scenes": [],
                    },
                    False,
                    0.1,
                ),
            ),
            patch("app.os.path.isfile", return_value=True),
            patch.object(
                self.app_module.tts_engine,
                "synthesize_lesson",
                side_effect=FileNotFoundError("TTS model files are missing."),
            ),
        ):
            response = self.client.post(
                "/api/generate_full_lesson",
                json={"topic": "Test topic", "target_length": 45},
            )

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.mimetype, "application/json")
        self.assertFalse(response.get_json()["success"])
        self.assertIn("TTS model files are missing", response.get_json()["error"])

    def test_selected_duration_reaches_tts_and_response_metadata(self):
        lesson = {
            "title": "A lesson",
            "level": "beginner",
            "language": "en",
            "scenes": [],
            "total_duration": 60,
        }

        with (
            tempfile.TemporaryDirectory() as output_dir,
            patch.object(self.app_module, "OUTPUT_DIR", output_dir),
            patch.object(self.app_module, "get_cache_key", return_value="test-key"),
            patch.object(self.app_module, "get_cached_lesson", return_value=None),
            patch("app.os.path.isfile", return_value=True),
            patch.object(
                self.app_module,
                "generate_lesson_plan",
                return_value=(lesson, False, 0.1),
            ) as planner,
            patch.object(
                self.app_module.tts_engine,
                "synthesize_lesson",
                return_value=(lesson, "captions.srt", 0.1),
            ) as tts,
            patch.object(self.app_module, "export_lesson_mp4", return_value=("lesson.mp4", 0.1)),
            patch.object(self.app_module, "save_to_cache"),
        ):
            response = self.client.post(
                "/api/generate_full_lesson",
                json={
                    "topic": "Test topic",
                    "target_length": 60,
                    "speed": 1.2,
                },
            )

        self.assertEqual(response.status_code, 200)
        planner.assert_called_once_with(
            topic="Test topic",
            level="beginner",
            language="en",
            target_length=60,
            speed=1.2,
        )
        self.assertEqual(tts.call_args.kwargs["target_duration"], 60)
        self.assertEqual(response.get_json()["lesson"]["target_duration"], 60)
        self.assertEqual(response.get_json()["metrics"]["actual_duration"], 60)

    def test_generation_reports_missing_tts_assets_before_planning(self):
        with (
            patch.object(self.app_module, "get_cache_key", return_value="uncached-key"),
            patch.object(self.app_module, "get_cached_lesson", return_value=None),
            patch.object(self.app_module.tts_engine, "model_path", "missing-model.onnx"),
            patch.object(self.app_module.tts_engine, "voices_path", "missing-voices.bin"),
            patch.object(self.app_module, "generate_lesson_plan") as planner,
        ):
            response = self.client.post(
                "/api/generate_full_lesson",
                json={"topic": "Test topic", "target_length": 45},
            )

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.mimetype, "application/json")
        self.assertIn("missing-model.onnx", response.get_json()["error"])
        planner.assert_not_called()

    def test_generation_rejects_invalid_json_body_with_json_response(self):
        response = self.client.post(
            "/api/generate_full_lesson",
            data="{",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.mimetype, "application/json")


class TopicDiversityTests(unittest.TestCase):
    def test_curated_topics_produce_distinct_content(self):
        from core.fallbacks import get_fallback_lesson

        p_loops = get_fallback_lesson("Python Loops", "en")
        p_photo = get_fallback_lesson("Photosynthesis", "en")
        p_binary = get_fallback_lesson("Binary Search", "en")
        p_gravity = get_fallback_lesson("Gravity", "en")

        titles = [p_loops["title"], p_photo["title"], p_binary["title"], p_gravity["title"]]
        self.assertEqual(len(titles), len(set(titles)))

        narrations = [
            p_loops["scenes"][1]["narration"],
            p_photo["scenes"][1]["narration"],
            p_binary["scenes"][1]["narration"],
            p_gravity["scenes"][1]["narration"]
        ]
        self.assertEqual(len(narrations), len(set(narrations)))

    def test_hindi_curated_topics_are_distinct(self):
        from core.fallbacks import get_fallback_lesson

        h_loops = get_fallback_lesson("Python Loops", "hi")
        h_binary = get_fallback_lesson("Binary Search", "hi")
        h_gravity = get_fallback_lesson("Gravity", "hi")

        self.assertNotEqual(h_loops["title"], h_binary["title"])
        self.assertNotEqual(h_binary["title"], h_gravity["title"])
        self.assertNotEqual(h_binary["scenes"][1]["narration"], h_gravity["scenes"][1]["narration"])

    def test_dynamic_fallback_handles_novel_topics_distinctly(self):
        from core.fallbacks import get_dynamic_fallback

        cs_plan = get_dynamic_fallback("Docker Containers", "en")
        physics_plan = get_dynamic_fallback("Quantum Entanglement", "en")

        self.assertIn("Docker", cs_plan["title"])
        self.assertIn("Quantum", physics_plan["title"])
        self.assertNotEqual(cs_plan["scenes"][1]["heading"], physics_plan["scenes"][1]["heading"])

    def test_curated_match_distinguishes_plant_cell_from_photosynthesis(self):
        from core.fallbacks import get_curated_fallback

        lesson = get_curated_fallback("Plant Cell")

        self.assertIn("Cell", lesson["title"])
        self.assertNotIn("Photosynthesis", lesson["title"])

    def test_curated_match_does_not_overgeneralize_specific_topics(self):
        from core.fallbacks import get_curated_fallback

        self.assertIsNone(get_curated_fallback("Newton's Method"))
        self.assertIsNone(get_curated_fallback("Mars"))
        self.assertIsNotNone(get_curated_fallback("Newton's 3rd Law of Motion"))
