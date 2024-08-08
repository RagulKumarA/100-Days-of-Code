# import colorgram
#
# colors = colorgram.extract('hirst_complete_spot.jpg',10)
#
# rgb_colors = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color =(r, g, b)
#     rgb_colors.append(color)
#
# print(rgb_colors)
import turtle
turtle.colormode(255)
import random

tim = turtle.Turtle()
tim.hideturtle()
colors = [(251, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140)]
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dots in range(1, number_of_dots + 1):
    #tim.pendown()
    tim.color(colors[random.randrange(0,10)])
    tim.dot(20)
    #tim.penup()
    tim.forward(50)
    #tim.pendown()

    if dots % 10 == 0:
        #tim.penup()
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
        #tim.pendown()










screen = turtle.Screen()
screen.exitonclick()



