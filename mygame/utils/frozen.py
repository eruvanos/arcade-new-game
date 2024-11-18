"""Utilities for frozen executables (e.g. PyInstaller)"""

import os
import sys
from pathlib import Path


def is_frozen():
    """https://pyinstaller.org/en/stable/runtime-information.html"""
    return getattr(sys, "frozen", False)


def get_resource_path(default_path: str = ".") -> Path:
    return Path(getattr(sys, "_MEIPASS", default_path)) / "resources"


def fix_cwd_for_frozen_execution():
    """Set cwd to pyinstaller extraction dir"""
    if is_frozen():
        os.chdir(Path(getattr(sys, "_MEIPASS", "..")))

def is_steamdeck() -> bool:
    """Check if the application is running on a Steam Deck.
    This does not check, if the game runs in Desktop mode"""
    return Path("/home/deck").exists()