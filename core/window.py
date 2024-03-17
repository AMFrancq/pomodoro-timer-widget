from tkinter import *
from tkinter import ttk
from core.timer import Timer


class Window:
    """
    A class used to create and manage a window with a timer.

    ...

    Attributes
    ----------
    root : Tk
        a Tk object that represents the main window
    timer : Timer
        a Timer object that represents the timer
    frm : ttk.Frame
        a Frame widget that contains the labels and buttons
    title_label : ttk.Label
        a Label widget that displays the title
    timer_label : ttk.Label
        a Label widget that displays the timer
    start_button : ttk.Button
        a Button widget that starts the timer
    pause_button : ttk.Button
        a Button widget that pauses the timer
    reset_button : ttk.Button
        a Button widget that resets the timer

    Methods
    -------
    create_frame():
        Creates and configures the main frame.
    create_labels():
        Creates the title and timer labels.
    create_buttons():
        Creates the start, pause, and reset buttons.
    run():
        Starts the Tkinter main loop.
    """

    def __init__(self):
        """Initializes Window with a root window, a timer, a frame, labels, and buttons."""
        self.root: Tk = Tk()
        self.timer: Timer = Timer()
        self.create_frame()
        self.create_labels()
        self.create_buttons()

    def create_frame(self):
        """Creates and configures the main frame."""
        self.frm: ttk.Frame = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.frm.columnconfigure(1, pad=10)
        self.frm.rowconfigure(0, pad=5)
        self.frm.rowconfigure(1, pad=5)
        self.frm.rowconfigure(2, pad=5)

    def create_labels(self):
        """Creates the title and timer labels."""
        self.title_label: ttk.Label = ttk.Label(
            self.frm, text="Pomodoro Timer")
        self.title_label.grid(column=1, row=0)
        self.timer_label: ttk.Label = ttk.Label(
            self.frm, text="25:00")
        self.timer_label.grid(column=1, row=1)

    def create_buttons(self):
        """Creates the start, pause, and reset buttons."""
        self.start_button: ttk.Button = ttk.Button(
            self.frm, text="Start",
            command=lambda: self.timer.start_timer(
                self.root, self.timer_label))
        self.start_button.grid(column=0, row=0)
        self.pause_button: ttk.Button = ttk.Button(
            self.frm, text="Pause",
            command=lambda: self.timer.stop_timer(
                self.root))
        self.pause_button.grid(column=0, row=1)
        self.reset_button: ttk.Button = ttk.Button(
            self.frm, text="Reset",
            command=lambda: self.timer.reset_timer(
                self.root, self.timer_label))
        self.reset_button.grid(column=0, row=2)

    def run(self):
        """Starts the Tkinter main loop."""
        self.root.mainloop()
