from tkinter import *
from tkinter import ttk
from timer import Timer


def create_window():
    root: Tk = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    frm.columnconfigure(1, pad=10)
    frm.rowconfigure(0, pad=5)
    frm.rowconfigure(1, pad=5)
    frm.rowconfigure(2, pad=5)
    ttk.Label(frm, text="Pomodoro Timer").grid(column=1, row=0)
    timerLabel = ttk.Label(frm, text="25:00")
    timerLabel.grid(column=1, row=1)
    timer: Timer = Timer()
    ttk.Button(frm, text="Start", command=lambda: timer.start_timer(
        root, timerLabel)).grid(column=0, row=0)
    ttk.Button(frm, text="Pause", command=lambda: timer.stop_timer(
        root)).grid(column=0, row=1)
    ttk.Button(frm, text="Reset", command=lambda: timer.reset_timer(
        root, timerLabel)).grid(column=0, row=2)
    root.mainloop()
