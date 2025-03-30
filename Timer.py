from turtle import *
import time

class Timer:
    def __init__(self):
        self.window = Screen()
        self.window.title("Таймер")
        self.window.setup(width=800, height=800)

        self.display = Turtle()
        self.display.hideturtle()
        self.display.penup()
        self.display.goto(0, 0)

        self.remaining_seconds = 0
        self.is_running = False
        self.callback = None

    def start_timer(self, seconds, callback):
        self.remaining_seconds = int(seconds)
        self.is_running = True
        self.callback = callback
        self.display.clear()
        self.countdown()

    def update_display(self):
        self.display.clear()
        mins, secs = divmod(self.remaining_seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        self.display.write(time_str, align="center", font=("Courier", 48, "bold"))

    def countdown(self):
        if self.remaining_seconds > -1 and self.is_running:
            self.update_display()
            self.remaining_seconds -= 1
            self.window.ontimer(self.countdown, 1000)
        else:
            self.display.clear()
            time.sleep(1)
            self.is_running = False
            self.clear()
            if self.callback:
                self.callback()

    def clear(self):
        self.display.clear()
        self.is_running = False
