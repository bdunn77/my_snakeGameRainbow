import turtle
from turtle import Turtle
import random

turtle.colormode(255)
class Food(Turtle):
    food_colors = ["white"]
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2, 2)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        self.color(random_color)
        self.food_colors.append(random_color)
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)

