# 터미널 출력 보조 함수가 입력 줄을 안정적으로 분리하는지 검증한다.
import unittest

from kana_trainer.cli import MAIN_MENU_OPTIONS
from kana_trainer.terminal import input_prompt, should_clear_screen


class TerminalRenderingTests(unittest.TestCase):
    def test_input_prompt_keeps_answer_on_its_own_line(self):
        self.assertEqual(input_prompt("し 의 읽는 법은?"), "し 의 읽는 법은?\n> ")

    def test_clear_screen_is_only_used_for_interactive_output(self):
        self.assertTrue(should_clear_screen(is_interactive=True, no_clear=False, supports_ansi=True))
        self.assertFalse(should_clear_screen(is_interactive=False, no_clear=False, supports_ansi=True))
        self.assertFalse(should_clear_screen(is_interactive=True, no_clear=True, supports_ansi=True))
        self.assertFalse(should_clear_screen(is_interactive=True, no_clear=False, supports_ansi=False))

    def test_main_menu_numbers_match_current_quiz_order(self):
        self.assertEqual(
            MAIN_MENU_OPTIONS,
            (
                ("1", "히라가나 보고 로마자 입력"),
                ("2", "가타카나 보고 로마자 입력"),
                ("3", "히라가나-가타카나 매칭"),
                ("4", "로마자 보고 히라가나 선택"),
                ("5", "조사 뜻 맞히기"),
                ("6", "헷갈리는 문자 선택"),
                ("7", "오답 복습"),
                ("8", "오답 기록 보기"),
                ("9", "학습 기록 보기"),
                ("10", "일본어.md 참고 자료 보기"),
                ("0", "종료"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
