from tkinter import Tk, ttk


class Timer:
    """
    A class used to create and manage a timer.

    ...

    Attributes
    ----------
    timer_event : str
        a string that represents the timer event
    stopped : bool
        a boolean that represents the timer state
    time : int
        an integer that represents the time in seconds
    rest_state : bool
        a boolean that represents the rest state

    Methods
    -------
    stop_timer(root):
        Stops the timer if it's running.
    reset_timer(root, timer_label):
        Resets the timer to its initial state.
    start_timer(root, timer_label):
        Starts the timer if it's not already running.
    countdown(root, timer_label):
        Counts down one second at a time.
    """

    def __init__(self):
        """Initializes Timer with a timer event, a timer state, a time, and a rest state."""
        self.timer_event = None
        self.stopped = False
        self.time = 1500  # Start with 25 minutes
        self.rest_state = False  # Start in work state

    def stop_timer(self, root: Tk):
        """Stops the timer if it's running."""
        if self.timer_event is not None:
            root.after_cancel(self.timer_event)
            self.timer_event = None
            self.stopped = True

    def reset_timer(self, root: Tk, timer_label: ttk.Label):
        """Resets the timer to its initial state."""
        if (self.timer_event is not None):
            root.after_cancel(self.timer_event)
            self.timer_event = None
        self.stopped = False
        self.time = 1500
        self.rest_state = False
        timer_label.configure(text="25:00")

    def start_timer(self, root: Tk, timer_label: ttk.Label):
        """Starts the timer if it's not already running."""
        if self.timer_event is None and not self.stopped:
            self.countdown(root, timer_label)
        elif self.timer_event is None and self.stopped:
            self.countdown(root, timer_label)
            self.stopped = False

    def countdown(self, root: Tk, timer_label: ttk.Label):
        """
        Counts down one second at a time.
        Switches between work and rest states when time is up.
        """
        if self.time > 0:
            self.time -= 1
            mins, secs = divmod(self.time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            timer_label.configure(text=time_format)
            self.timer_event = root.after(
                1000, self.countdown, root, timer_label)
        else:
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
