# GUI 표시 폰트 선택 정책을 검증한다.
import unittest

import tkinter as tk

from kana_trainer.gui import KanaTrainerApp, choose_display_font


class GuiFontTests(unittest.TestCase):
    def test_choose_display_font_prefers_nanum_gothic(self):
        available = ("MS Gothic", "Meiryo", "Yu Gothic UI", "나눔고딕")

        self.assertEqual(choose_display_font(available), "나눔고딕")

    def test_choose_display_font_falls_back_to_yu_gothic_then_meiryo(self):
        self.assertEqual(choose_display_font(("MS Gothic", "Meiryo", "Yu Gothic UI")), "Yu Gothic UI")
        self.assertEqual(choose_display_font(("MS Gothic", "Meiryo")), "Meiryo")
        self.assertEqual(choose_display_font(("Arial", "MS Gothic")), "MS Gothic")

    def test_entry_stays_visible_with_large_font_size(self):
        root = tk.Tk()
        try:
            app = KanaTrainerApp(root)
            root.update()
            app.text_font.configure(size=50)

            root.update_idletasks()

            self.assertTrue(app.entry.master.winfo_ismapped())
            self.assertTrue(app.entry.winfo_ismapped())
        finally:
            root.destroy()

    def test_submit_returns_focus_to_entry(self):
        root = tk.Tk()
        try:
            app = KanaTrainerApp(root)
            calls = []
            app.handler = lambda _value: None
            app.focus_entry = lambda: calls.append("focused")
            app.entry_var.set("shi")

            app.submit_input()

            self.assertEqual(calls, ["focused"])
        finally:
            root.destroy()

    def test_semantic_color_tags_are_configured(self):
        root = tk.Tk()
        try:
            app = KanaTrainerApp(root)

            self.assertEqual(app.output.tag_cget("question", "foreground"), "#F2D06B")
            self.assertEqual(app.output.tag_cget("input", "foreground"), "#7DD3C7")
            self.assertEqual(app.output.tag_cget("result", "foreground"), "#C7A9FF")
        finally:
            root.destroy()

    def test_menu_numbers_use_menu_color_tag(self):
        root = tk.Tk()
        try:
            app = KanaTrainerApp(root)
            root.update()

            self.assertIn("menu", app.output.tag_names("3.0"))
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
