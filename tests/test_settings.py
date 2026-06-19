# GUI 앱 설정 저장과 보정 동작을 검증한다.
import tempfile
import unittest
from pathlib import Path

from kana_trainer.settings import AppSettings, SettingsStore, clamp_font_size, window_geometry


class SettingsTests(unittest.TestCase):
    def test_missing_settings_file_uses_default_font_size(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            store = SettingsStore(Path(temp_dir) / "settings.json")

            settings = store.load()

        self.assertEqual(settings.font_size, 24)
        self.assertEqual(settings.window_width, 920)
        self.assertEqual(settings.window_height, 680)

    def test_saved_font_size_can_be_loaded_again(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            store = SettingsStore(Path(temp_dir) / "settings.json")

            store.save(AppSettings(font_size=36))
            settings = store.load()

        self.assertEqual(settings.font_size, 36)

    def test_saved_window_size_can_be_loaded_again(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            store = SettingsStore(Path(temp_dir) / "settings.json")

            store.save(AppSettings(window_width=1110, window_height=740))
            settings = store.load()

        self.assertEqual(settings.window_width, 1110)
        self.assertEqual(settings.window_height, 740)

    def test_saved_window_position_can_be_loaded_again(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            store = SettingsStore(Path(temp_dir) / "settings.json")

            store.save(AppSettings(window_x=120, window_y=80))
            settings = store.load()

        self.assertEqual(settings.window_x, 120)
        self.assertEqual(settings.window_y, 80)

    def test_window_geometry_uses_saved_size(self):
        settings = AppSettings(window_width=1110, window_height=740)

        self.assertEqual(window_geometry(settings), "1110x740")

    def test_window_geometry_uses_saved_size_and_position(self):
        settings = AppSettings(window_width=1110, window_height=740, window_x=120, window_y=80)

        self.assertEqual(window_geometry(settings), "1110x740+120+80")

    def test_window_geometry_preserves_negative_position(self):
        settings = AppSettings(window_width=900, window_height=600, window_x=-120, window_y=40)

        self.assertEqual(window_geometry(settings), "900x600-120+40")

    def test_font_size_is_clamped_to_gui_bounds(self):
        self.assertEqual(clamp_font_size(5), 12)
        self.assertEqual(clamp_font_size(50), 50)
        self.assertEqual(clamp_font_size(100), 72)


if __name__ == "__main__":
    unittest.main()
