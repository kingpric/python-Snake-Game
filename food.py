from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-13, 13) * 20
        rand_y = random.randint(-13, 13) * 20
        self.goto(rand_x, rand_y)
