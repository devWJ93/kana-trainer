# GUI 표시 폰트 선택 정책을 검증한다.
import unittest

from kana_trainer.gui import choose_display_font


class GuiFontTests(unittest.TestCase):
    def test_choose_display_font_prefers_nanum_gothic(self):
        available = ("MS Gothic", "Meiryo", "Yu Gothic UI", "나눔고딕")

        self.assertEqual(choose_display_font(available), "나눔고딕")

    def test_choose_display_font_falls_back_to_yu_gothic_then_meiryo(self):
        self.assertEqual(choose_display_font(("MS Gothic", "Meiryo", "Yu Gothic UI")), "Yu Gothic UI")
        self.assertEqual(choose_display_font(("MS Gothic", "Meiryo")), "Meiryo")
        self.assertEqual(choose_display_font(("Arial", "MS Gothic")), "MS Gothic")


if __name__ == "__main__":
    unittest.main()
