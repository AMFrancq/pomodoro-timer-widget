from tkinter import Tk, ttk

class Timer:
    def __init__(self):
        self.timer_event = None
        self.stopped = False
        self.time = 1500
        self.rest_state = False

    def stop_timer(self, root: Tk, timer_label: ttk.Label):
        pass

    def reset_timer(self, root: Tk, timer_label: ttk.Label):
        pass

    def countdown(self, root: Tk, timer_label: ttk.Label):
        if self.time > 0:
            self.time -= 1
            mins, secs = divmod(self.time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            timer_label.configure(text=time_format)
            self.timer_event = root.after(1000, self.countdown, root, timer_label)
        else:
            if(self.rest_state):
                timer_label.configure(text="25:00")
                self.rest_state = False
                self.time = 1500
                self.timer_event = root.after(1000, self.countdown, root, timer_label)
            else:
                timer_label.configure(text="05:00")
                self.rest_state = True
                self.time = 300
                self.timer_event = root.after(1000, self.countdown, root, timer_label)

    def start_timer(self, root: Tk, timer_label: ttk.Label):
        if self.timer_event is None and not self.stopped:
            self.countdown(root, timer_label)
        elif self.timer_event is None and self.stopped:
            self.countdown(root, timer_label)
            self.stopped = False
            self.stopped_time = 0