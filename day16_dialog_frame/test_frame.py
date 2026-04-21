import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames
    print("Number of frames on a page:", len(frames))  # 7