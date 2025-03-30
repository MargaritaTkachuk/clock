from time import strftime
from turtle import *
from math import *
import time

class Watch:
    def show_time(self):
        pass

class Number:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def draw(self):
        penup()
        goto(self.x, self.y)
        write(self.n, move=False, align="left", font=("Arial", 24, "bold"))

    def clear(self):
        penup()
        goto(self.x, self.y)
        clear()

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

    def show_time(self):
        self.draw_clock_face()  # Draw the clock face
        self.update_time()
        ontimer(self.show_time, 1000)

    def clear(self):
        penup()
        goto(10, -self.r + 10)
        pendown()
        clear()  # Clear the whole analog clock

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

class DigitalWatch(Watch):  # Треба прибрати Цифровий годинник і реалізувати його показ кнопкою
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Digital Clock")

        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color("green")
        self.pen.penup()
        self.pen.goto(0, 0)

    def update_time(self):
        self.pen.undo()
        current_time = strftime("%H:%M:%S")
        self.pen.write(current_time, align="center", font=("Courier", 40, "bold"))
        self.screen.ontimer(self.update_time, 1000)

    def show_time(self):
        self.update_time()
        self.screen.mainloop()

if __name__ == '__main__':
    reset()
    speed(0)
    hideturtle()
    watch = AnalogWatch(200)
    watch.show_time()
    watch = DigitalWatch()
    watch.show_time()
    mainloop()
