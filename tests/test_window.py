import unittest
from unittest.mock import patch, MagicMock
from src.window import Window


class TestWindow(unittest.TestCase):
    @patch('src.window.Tk')
    @patch('src.window.Timer')
    def setUp(self, mock_timer, mock_tk):
        self.mock_timer = mock_timer
        self.mock_tk = mock_tk
        self.window = Window()
        self.window.frm.grid = MagicMock()
        self.window.title_label.grid = MagicMock()
        self.window.timer_label.grid = MagicMock()
        self.window.start_button.grid = MagicMock()
        self.window.pause_button.grid = MagicMock()
        self.window.reset_button.grid = MagicMock()

    def test_create_frame(self):
        self.window.create_frame()
        self.window.frm.grid.assert_called_once()

    def test_create_labels(self):
        self.window.create_labels()
        self.window.title_label.grid.assert_called_once_with(column=1, row=0)
        self.window.timer_label.grid.assert_called_once_with(column=1, row=1)

    def test_create_buttons(self):
        self.window.create_buttons()
        self.window.start_button.grid.assert_called_once_with(column=0, row=0)
        self.window.pause_button.grid.assert_called_once_with(column=0, row=1)
        self.window.reset_button.grid.assert_called_once_with(column=0, row=2)

    def test_run(self):
        self.window.root.mainloop = MagicMock()
        self.window.run()
        self.window.root.mainloop.assert_called_once()
