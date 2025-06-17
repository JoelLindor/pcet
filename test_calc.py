import logging

import pytest
from calc import build_gui

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture(scope="module")
def gui_app():
    result = {"action": None}

    def on_keypress(action):
        result["action"] = action

    root = build_gui(on_keypress=on_keypress)
    logger.info("GUI launched for testing.")
    root.update()  # Process pending events

    # Set focus to root for key events to work
    root.focus_force()

    yield root, result
    root.destroy()


def test_ctrl_a_binding(gui_app):
    root, result = gui_app
    logger.info("Sending a ctrl-a keybind")
    root.event_generate("<Control-a>")
    root.update()
    assert result["action"] == 1


def test_ctrl_s_binding(gui_app):
    root, result = gui_app
    logger.info("Sending a ctrl-s keybind")
    root.event_generate("<Control-s>")
    root.update()
    assert result["action"] == 2


def test_ctrl_m_binding(gui_app):
    root, result = gui_app
    logger.info("Sending a ctrl-m keybind")
    root.event_generate("<Control-m>")
    root.update()
    assert result["action"] == 3


def test_ctrl_d_binding(gui_app):
    root, result = gui_app
    logger.info("Sending a ctrl-d keybind")
    root.event_generate("<Control-d>")
    root.update()
    assert result["action"] == 4
