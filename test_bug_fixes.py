import hashlib
import unittest
from unittest.mock import patch

from core.cache_manager import get_cache_key


class CacheKeyTests(unittest.TestCase):
    def test_default_settings_keep_existing_cache_keys(self):
        raw = "photosynthesis_hi_beginner_hf_alpha"
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
