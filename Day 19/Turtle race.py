import random
from turtle import Turtle, Screen

is_on_race = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-60, -30, 0, 30, 60, 90]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axis[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_on_race = True

while is_on_race:

    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_on_race = False
            winning_color = turtle.pencolor()
            if user_bet.lower() == winning_color.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
