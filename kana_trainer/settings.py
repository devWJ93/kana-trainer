# GUI 앱의 사용자 설정을 저장하고 불러온다.
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

MIN_FONT_SIZE = 12
MAX_FONT_SIZE = 72
DEFAULT_FONT_SIZE = 24
MIN_WINDOW_WIDTH = 680
MIN_WINDOW_HEIGHT = 460
DEFAULT_WINDOW_WIDTH = 920
DEFAULT_WINDOW_HEIGHT = 680


@dataclass(frozen=True)
class AppSettings:
    font_size: int = DEFAULT_FONT_SIZE
    window_width: int = DEFAULT_WINDOW_WIDTH
    window_height: int = DEFAULT_WINDOW_HEIGHT
    window_x: int | None = None
    window_y: int | None = None


def default_settings_path() -> Path:
    return Path.home() / ".kana-trainer" / "settings.json"


def clamp_font_size(value: int) -> int:
    return max(MIN_FONT_SIZE, min(MAX_FONT_SIZE, value))


def clamp_window_width(value: int) -> int:
    return max(MIN_WINDOW_WIDTH, value)


def clamp_window_height(value: int) -> int:
    return max(MIN_WINDOW_HEIGHT, value)


def parse_optional_int(value: object) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def format_window_position(x: int, y: int) -> str:
    x_part = f"+{x}" if x >= 0 else str(x)
    y_part = f"+{y}" if y >= 0 else str(y)
    return f"{x_part}{y_part}"


def window_geometry(settings: AppSettings) -> str:
    width = clamp_window_width(settings.window_width)
    height = clamp_window_height(settings.window_height)
    if settings.window_x is not None and settings.window_y is not None:
        return f"{width}x{height}{format_window_position(settings.window_x, settings.window_y)}"
    return f"{width}x{height}"


class SettingsStore:
    def __init__(self, path: Path | None = None):
        self.path = path or default_settings_path()

    def load(self) -> AppSettings:
        if not self.path.exists():
            return AppSettings()
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError):
            return AppSettings()
        if not isinstance(data, dict):
            return AppSettings()
        try:
            font_size = int(data.get("font_size", DEFAULT_FONT_SIZE))
        except (TypeError, ValueError):
            font_size = DEFAULT_FONT_SIZE
        try:
            window_width = int(data.get("window_width", DEFAULT_WINDOW_WIDTH))
        except (TypeError, ValueError):
            window_width = DEFAULT_WINDOW_WIDTH
        try:
            window_height = int(data.get("window_height", DEFAULT_WINDOW_HEIGHT))
        except (TypeError, ValueError):
            window_height = DEFAULT_WINDOW_HEIGHT
        window_x = parse_optional_int(data.get("window_x"))
        window_y = parse_optional_int(data.get("window_y"))
        return AppSettings(
            font_size=clamp_font_size(font_size),
            window_width=clamp_window_width(window_width),
            window_height=clamp_window_height(window_height),
            window_x=window_x,
            window_y=window_y,
        )

    def save(self, settings: AppSettings) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "font_size": clamp_font_size(settings.font_size),
            "window_width": clamp_window_width(settings.window_width),
            "window_height": clamp_window_height(settings.window_height),
            "window_x": settings.window_x,
            "window_y": settings.window_y,
        }
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
