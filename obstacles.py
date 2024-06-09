import turtle as t
from turtle import Turtle, Screen
import random

screen = Screen()
class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        
    def random_clr(self):
        t.colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tpl = (r, g, b)
        return tpl
    
    def create_cars(self):
        screen.tracer(0)
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('square')
        y = random.randint(-265, 265)
        new_turtle.goto(500, y)
        new_turtle.shapesize(1, 3, 1)
        new_turtle.color(self.random_clr())
        self.car_list.append(new_turtle)