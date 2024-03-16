import unittest
from unittest.mock import MagicMock
from tkinter import Tk, ttk
from src.timer import Timer


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.timer_label = ttk.Label(self.root)
        self.timer = Timer()

    def tearDown(self):
        self.root.destroy()

    def test_stop_timer(self):
        # Mock the after method
        self.root.after = MagicMock()

        # Test stop_timer method when timer_event is None
        self.timer.stop_timer(self.root)
        self.assertFalse(self.timer.stopped)

        # Test stop_timer method when timer_event is not None
        self.timer.timer_event = self.root.after(
            1000, self.timer.countdown, self.root, self.timer_label)
        self.timer.stop_timer(self.root)
        self.assertTrue(self.timer.stopped)
        self.assertIsNone(self.timer.timer_event)
        self.root.after.assert_called_once_with(
            1000, self.timer.countdown, self.root, self.timer_label)

    def test_reset_timer(self):
        # Mock the after method
        self.root.after = MagicMock()
        self.root.after_cancel = MagicMock()
        self.timer_label.configure = MagicMock()

        # Test reset_timer method when timer_event is None
        self.timer.reset_timer(self.root, self.timer_label)
        self.root.after_cancel.assert_not_called()

        # Test reset_timer method when timer_event is not None
        self.timer_label.configure.reset_mock()
        self.timer.timer_event = self.root.after(
            1000, self.timer.countdown, self.root, self.timer_label)
        self.timer.reset_timer(self.root, self.timer_label)
        self.assertFalse(self.timer.stopped)
        self.assertEqual(self.timer.time, 1500)
        self.assertFalse(self.timer.rest_state)
        self.assertIsNone(self.timer.timer_event)
        self.timer_label.configure.assert_called_once_with(text="25:00")

    def test_start_timer(self):
        # Mock the after method
        self.timer.countdown = MagicMock()

        # Test start_timer method when timer is not already running and not stopped
        self.timer.start_timer(self.root, self.timer_label)
        self.timer.countdown.assert_called_once_with(
            self.root, self.timer_label)

        # Test start_timer method when timer is not already running and stopped
        self.timer.countdown.reset_mock()
        self.timer.stopped = True
        self.timer.start_timer(self.root, self.timer_label)
        self.assertFalse(self.timer.stopped)
        self.timer.countdown.assert_called_once_with(
            self.root, self.timer_label)

        # Test start_timer method when timer is already running
        self.timer.countdown.reset_mock()
        self.timer.timer_event = 1
        self.timer.start_timer(self.root, self.timer_label)
        self.timer.countdown.assert_not_called()

    def test_countdown(self):
        # Mock the after method
        self.root.after = MagicMock()
        self.timer_label.configure = MagicMock()

        # Test countdown method when time is greater than 0
        self.timer.time = 5
        self.timer.countdown(self.root, self.timer_label)
        self.assertEqual(self.timer.time, 4)
        self.timer_label.configure.assert_called_once_with(text="00:04")
        self.root.after.assert_called_once_with(
            1000, self.timer.countdown, self.root, self.timer_label)

        # Test countdown method when time is 0 and rest_state is False
        self.root.after.reset_mock()
        self.timer_label.configure.reset_mock()
        self.timer.time = 0
        self.timer.rest_state = False
        self.timer.countdown(self.root, self.timer_label)
        self.assertTrue(self.timer.rest_state)
        self.assertEqual(self.timer.time, 300)
        self.timer_label.configure.assert_called_once_with(text="05:00")
        self.root.after.assert_called_with(
            1000, self.timer.countdown, self.root, self.timer_label)

        # Test countdown method when time is 0 and rest_state is True
        self.root.after.reset_mock()
        self.timer_label.configure.reset_mock()
        self.timer.time = 0
        self.timer.rest_state = True
        self.timer.countdown(self.root, self.timer_label)
        self.assertFalse(self.timer.rest_state)
        self.assertEqual(self.timer.time, 1500)
        self.timer_label.configure.assert_called_once_with(text="25:00")
        self.root.after.assert_called_with(
            1000, self.timer.countdown, self.root, self.timer_label)


if __name__ == '__main__':
    unittest.main()
