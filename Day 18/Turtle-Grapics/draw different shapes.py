from turtle import Turtle, Screen
import random
tim = Turtle()
colors = ["cyan","blue","lime","gold","crimson","magenta","dark violet","hot pink","light coral","aquamarine"]
def power(sides):
    for i in range(sides):
        tim.forward(100)
        tim.right( 360 / sides)
for i in range(3,9):
    tim.color(random.choice(colors))
    power(i)























screen = Screen()
screen.exitonclick()