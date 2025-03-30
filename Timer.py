from turtle import *
import time


class Timer:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Таймер")
        self.screen.tracer(0)

        self.display = Turtle()
        self.display.hideturtle()
        self.display.penup()
        self.display.goto(0, 0)

        self.remaining_seconds = 0
        self.is_running = False

        self.setup_timer()

    def setup_timer(self):
        self.display.clear()
        self.display.write("Встановлення таймера...",
                           align="center", font=("Courier", 16, "normal"))
        self.screen.update()

        seconds = self.screen.numinput("Таймер",
                                       "Введіть кількість секунд (1-3600):",
                                       default=10, minval=1, maxval=3600)

        if seconds:
            self.remaining_seconds = int(seconds)
            self.start_timer()
        else:
            self.display.clear()
            self.display.write("Таймер скасовано",
                               align="center", font=("Courier", 16, "normal"))
            self.screen.update()

    def update_display(self):
        self.display.clear()
        mins, secs = divmod(self.remaining_seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        self.display.write(time_str, align="center", font=("Courier", 48, "bold"))
        self.screen.update()

    def start_timer(self):
        self.is_running = True
        self.countdown()

    def countdown(self):
        while self.remaining_seconds > 0 and self.is_running:
            self.update_display()
            time.sleep(1)
            self.remaining_seconds -= 1

        if self.remaining_seconds <= 0:
            self.display.clear()
            self.display.write("Час вийшов!",
                               align="center", font=("Courier", 36, "bold"))
            self.screen.update()
            self.is_running = False

    def run(self):
        self.screen.mainloop()


if __name__ == "__main__":
    timer = Timer()
    timer.run()