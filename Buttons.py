from time import strftime
from turtle import *
from math import *
import time
from Timer import Timer

class Buttons:
    def __init__(self, analog_watch, digital_watch):
        self.analog_watch = analog_watch
        self.digital_watch = digital_watch
        self.is_analog = True
        self.create_buttons()
        # self.timer = Timer()

    def create_buttons(self):
        self.analog_button = self.create_button(-150, -250, "Зміна формату годинника", self.switch_watch)
        self.exit_button = self.create_button(150, -250, "Закрити програму", self.exit_program)
        self.change_format = self.create_button(-150, -300, "Змінити 12/24", self.change)
        # self.timer_button = self.create_button(0, -300, "Встановити таймер", self.start_timer)

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
        button.write(text, align="center", font=("Courier", 14, "bold"))
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

    def start_timer(self, x, y):
        Timer()
        # self.timer.setup_timer()
        # if self.timer.active:
        #     self.timer.countdown()

    def change(self, x, y):
        if not self.is_analog:
            self.digital_watch.toggle_format(x, y)

    def exit_program(self, x, y):
        bye()