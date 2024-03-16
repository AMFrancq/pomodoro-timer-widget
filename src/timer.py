from tkinter import Tk, ttk


class Timer:
    def __init__(self):
        # Initialize timer state
        self.timer_event = None
        self.stopped = False
        self.time = 1500  # Start with 25 minutes
        self.rest_state = False  # Start in work state

    def stop_timer(self, root: Tk):
        # Stop the timer if it's running
        if self.timer_event is not None:
            root.after_cancel(self.timer_event)
            self.timer_event = None
            self.stopped = True

    def reset_timer(self, root: Tk, timer_label: ttk.Label):
        # Reset the timer to its initial state
        if (self.timer_event is not None):
            root.after_cancel(self.timer_event)
            self.timer_event = None
        self.stopped = False
        self.time = 1500
        self.rest_state = False
        timer_label.configure(text="25:00")

    def start_timer(self, root: Tk, timer_label: ttk.Label):
        # Start the timer if it's not already running
        if self.timer_event is None and not self.stopped:
            self.countdown(root, timer_label)
        elif self.timer_event is None and self.stopped:
            self.countdown(root, timer_label)
            self.stopped = False

    def countdown(self, root: Tk, timer_label: ttk.Label):
        # Countdown one second at a time
        if self.time > 0:
            self.time -= 1
            mins, secs = divmod(self.time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            timer_label.configure(text=time_format)
            self.timer_event = root.after(
                1000, self.countdown, root, timer_label)
        else:
            # Switch between work and rest states
            if (self.rest_state):
                timer_label.configure(text="25:00")
                self.rest_state = False
                self.time = 1500
                self.timer_event = root.after(
                    1000, self.countdown, root, timer_label)
            else:
                timer_label.configure(text="05:00")
                self.rest_state = True
                self.time = 300
                self.timer_event = root.after(
                    1000, self.countdown, root, timer_label)
