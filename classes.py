from time import strftime
from turtle import *
from math import *
import time

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
        write(self.n, move=False, align="left", font=("Arial", 24, "bold"))

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

    def update_time(self):
        if not self.active:
            return
        self.pen.clear()
        current_time = strftime("%H:%M:%S")
        self.pen.write(current_time, align="center", font=("Courier", 40, "bold"))
        self.timer = ontimer(self.update_time, 1000)

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

class Buttons:
    def __init__(self, analog_watch, digital_watch):
        self.analog_watch = analog_watch
        self.digital_watch = digital_watch
        self.is_analog = True
        self.create_buttons()

    def create_buttons(self):
        self.analog_button = self.create_button(-150, -250, "Зміна формату годинника", self.switch_watch)
        self.exit_button = self.create_button(150, -250, "Закрити програму", self.exit_program)

    def create_button(self, x, y, text, action):
        hitbox = Turtle()
        hitbox.penup()
        hitbox.goto(x, y)
        hitbox.shape("square")
        hitbox.shapesize(stretch_wid=2, stretch_len=13)
        hitbox.pensize(2)
        hitbox.pencolor("black")
        hitbox.fillcolor("")
        hitbox.onclick(action)
        button = Turtle()
        button.hideturtle()
        button.penup()
        button.goto(x, y - 10)
        button.write(text, align="center", font=("Arial", 14, "bold"))
        button.onclick(action)
        return button

    def switch_watch(self, x, y):
        if self.is_analog:
            self.analog_watch.clear()
            self.analog_watch.stop_time()
            self.digital_watch.show_time()
        else:
            self.digital_watch.clear()
            self.digital_watch.stop_time()
            self.analog_watch.show_time()
        self.is_analog = not self.is_analog

    def exit_program(self, x, y):
        bye()

if __name__ == '__main__':
    speed(0)
    hideturtle()
    analog_watch = AnalogWatch(200)
    digital_watch = DigitalWatch()
    buttons = Buttons(analog_watch, digital_watch)
    analog_watch.show_time()
    mainloop()
