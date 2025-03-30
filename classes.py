from time import strftime
from turtle import *
from math import *
import time
from Buttons import Buttons

class Watch:
    def show_time(self):
        pass

    def stop_time(self):
        pass

class Number:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def draw(self):
        penup()
        goto(self.x, self.y)
        write(self.n, move=False, align="left", font=("Courier", 24, "bold"))

class AnalogWatch(Watch):
    def __init__(self, size):
        self.r = size
        self.numbers = []
        self.sec = Hand(0.8 * size, 2, 'black')
        self.min = Hand(0.7 * size, 4, 'black')
        self.hour = Hand(0.5 * size, 6, 'black')
        self.generate_numbers()
        self.hands = Turtle()
        self.hands.hideturtle()
        self.hands.speed(0)
        self.timer = None
        self.active = False
        tracer(0)

    def generate_numbers(self):
        for i in range(1, 13):
            x = self.r * sin(((pi / 6) + 2 * pi * i) / 12) * 0.8
            y = self.r * cos(((pi / 6) + 2 * pi * i) / 12) * 0.8
            self.numbers.append(Number(i, x, y))

    def draw_clock_face(self):
        penup()
        goto(10, -self.r + 10)
        pendown()
        pensize(6)
        circle(self.r)
        for n in self.numbers:
            n.draw()

    def update_time(self):
        if not self.active:
            return
        self.sec.clear()
        self.min.clear()
        self.hour.clear()
        now = time.localtime()
        sec_angle = now.tm_sec * 6
        min_angle = now.tm_min * 6 + now.tm_sec * 0.1
        hour_angle = (now.tm_hour % 12) * 30 + now.tm_min * 0.5
        self.sec.draw(sec_angle)
        self.min.draw(min_angle)
        self.hour.draw(hour_angle)
        update()
        self.timer = ontimer(self.update_time, 1000)

    def show_time(self):
        self.active = True
        self.draw_clock_face()
        self.update_time()

    def stop_time(self):
        self.active = False
        if self.timer:
            ontimer(None, self.timer)
            self.timer = None

    def clear(self):
        self.stop_time()
        clear()
        self.sec.clear()
        self.min.clear()
        self.hour.clear()

class Hand:
    def __init__(self, lent, wid, col):
        self.h = Turtle()
        self.h.hideturtle()
        self.h.speed(0)
        self.lent = lent
        self.wid = wid
        self.col = col

    def draw(self, ang):
        self.h.penup()
        self.h.goto(0, 0)
        self.h.setheading(90 - ang)
        self.h.pendown()
        self.h.pensize(self.wid)
        self.h.pencolor(self.col)
        self.h.forward(self.lent)

    def clear(self):
        self.h.clear()

class DigitalWatch(Watch):
    def __init__(self):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color("green")
        self.pen.penup()
        self.pen.goto(0, 0)
        self.timer = None
        self.active = False
        self.is_24_hour_format = True

    def update_time(self):
        if not self.active:
            return
        self.pen.clear()
        current_time = strftime("%H:%M:%S") if self.is_24_hour_format else strftime("%I:%M:%S %p")
        self.pen.write(current_time, align="center", font=("Courier", 40, "bold"))
        self.timer = ontimer(self.update_time, 1000)

    def toggle_format(self, x=None, y=None):
        self.is_24_hour_format = not self.is_24_hour_format
        self.update_time()

    def show_time(self):
        self.active = True
        self.update_time()

    def stop_time(self):
        self.active = False
        if self.timer:
            ontimer(None, self.timer)
            self.timer = None

    def clear(self):
        self.stop_time()
        self.pen.clear()


if __name__ == '__main__':
    speed(0)
    hideturtle()
    analog_watch = AnalogWatch(200)
    digital_watch = DigitalWatch()
    buttons = Buttons(analog_watch, digital_watch)
    analog_watch.show_time()
    mainloop()
