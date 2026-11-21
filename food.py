from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
