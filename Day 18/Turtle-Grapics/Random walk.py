import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.pensize(10)
direction = [90,180,270,0]

def random_color(red = 0,):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(1000):
    tim.speed(100)
    tim.forward(10)
    tim.setheading(random.choice(direction))
    tim.color(random_color())
screen = Screen()
screen.exitonclick()
