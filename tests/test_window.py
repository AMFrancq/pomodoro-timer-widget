import unittest
from unittest.mock import MagicMock
from tkinter import ttk
from core.window import Window


class TestWindow(unittest.TestCase):
    def setUp(self):
        """Sets up the test environment before each test."""
        self.window = Window()

    def test_create_frame(self):
        """
        Tests the create_frame method.
        Checks that the frame is created and configured correctly.
        """
        self.assertIsInstance(self.window.frm, ttk.Frame)
        self.assertEqual(str(self.window.frm['padding'][0]), '10')

    def test_create_labels(self):
        """
        Tests the create_labels method.
        Checks that the title and timer labels are created correctly and placed in the correct grid.
        """
        self.assertIsInstance(self.window.title_label, ttk.Label)
        self.assertEqual(self.window.title_label['text'], 'Pomodoro Timer')
        self.assertEqual(self.window.title_label.grid_info()['column'], 1)
        self.assertEqual(self.window.title_label.grid_info()['row'], 0)
        self.assertIsInstance(self.window.timer_label, ttk.Label)
        self.assertEqual(self.window.timer_label['text'], '25:00')
        self.assertEqual(self.window.timer_label.grid_info()['column'], 1)
        self.assertEqual(self.window.timer_label.grid_info()['row'], 1)

    def test_create_buttons(self):
        """
        Tests the create_buttons method.
        Checks that the start, pause, and reset buttons are created correctly and placed in the correct grid.
        """
        self.assertIsInstance(self.window.start_button, ttk.Button)
        self.assertEqual(self.window.start_button['text'], 'Start')
        self.assertEqual(self.window.start_button.grid_info()['column'], 0)
        self.assertEqual(self.window.start_button.grid_info()['row'], 0)
        self.assertIsInstance(self.window.pause_button, ttk.Button)
        self.assertEqual(self.window.pause_button['text'], 'Pause')
        self.assertEqual(self.window.pause_button.grid_info()['column'], 0)
        self.assertEqual(self.window.pause_button.grid_info()['row'], 1)
        self.assertIsInstance(self.window.reset_button, ttk.Button)
        self.assertEqual(self.window.reset_button['text'], 'Reset')
        self.assertEqual(self.window.reset_button.grid_info()['column'], 0)
        self.assertEqual(self.window.reset_button.grid_info()['row'], 2)

    def test_run(self):
        """
        Tests the run method.
        Checks that the Tkinter main loop is started.
        """
        self.window.root.mainloop = MagicMock()
        self.window.run()
        self.window.root.mainloop.assert_called_once()
