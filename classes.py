from turtle import *
from math import *
import time

class Number:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def draw(self):
        penup()
        goto(self.x, self.y)
        write(self.n, move=False, align="left", font=("Impact", 22, "bold"))


class ClockFace:
    def __init__(self, r):
        self.numbers = []
        self.r = r
        self.generate_numbers()

    def generate_numbers(self):
        for i in range(1, 13):
            x = self.r * sin(((pi / 6) + 2 * pi * i) / 12) * 0.8
            y = self.r * cos(((pi / 6) + 2 * pi * i) / 12) * 0.8
            self.numbers.append(Number(i, x, y))

    def draw(self):
        penup()
        goto(10, -self.r + 10)
        pendown()
        pensize(6)
        circle(self.r)
        for n in self.numbers:
            n.draw()


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

class AnalogWatch:
    def __init__(self, size):
        self.sec = Hand(0.8 * size, 2, 'black')
        self.min = Hand(0.7 * size, 4, 'black')
        self.hour = Hand(0.5 * size, 6, 'black')
        self.hands = Turtle()
        self.hands.hideturtle()
        self.hands.speed(0)
        tracer(0)

    def show_time(self):
        while True:
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
            time.sleep(1)



if __name__ == '__main__':
    reset()
    speed(0)
    hideturtle()
    # number = Number(666, 0, 0)
    # number.draw()
    c = ClockFace(200)
    c.draw()
    watch = AnalogWatch(200)
    watch.show_time()
    mainloop()


