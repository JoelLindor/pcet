import pytest
from calc import build_gui


@pytest.fixture
def gui_app():
    result = {"action": None}

    def on_keypress(action):
        result["action"] = action

    root = build_gui(on_keypress=on_keypress)
    root.withdraw()  # Hide the GUI window for testing
    root.update()  # Process pending GUI events

    # Ensure window can receive key events
    root.focus_force()
    root.update()

    yield root, result

    root.destroy()


def test_ctrl_a_binding(gui_app):
    root, result = gui_app
    root.event_generate("<Control-a>")
    root.update()
    assert result["action"] == 1


def test_ctrl_s_binding(gui_app):
    root, result = gui_app
    root.event_generate("<Control-s>")
    root.update()
    assert result["action"] == 2


def test_ctrl_m_binding(gui_app):
    root, result = gui_app
    root.event_generate("<Control-m>")
    root.update()
    assert result["action"] == 3


def test_ctrl_d_binding(gui_app):
    root, result = gui_app
    root.event_generate("<Control-d>")
    root.update()
    assert result["action"] == 4
