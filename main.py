import turtle as turtle_modules
from turtle import *
import colorgram
import random

turtle_modules.colormode(255)

def get_color():
    colors = colorgram.extract('image.jpg', 15)
    rgb_storage = []
    for color in colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        rgb_storage.append((r, g, b))
    return rgb_storage


x = -320
y = -300
tim = turtle_modules.Turtle()
tim.speed('fastest')
tim.hideturtle()
color_bank = get_color()
for j in range(10):

    tim.penup()
    tim.setpos(x, y)

    for i in range(10):
        tim.dot(20, random.choice(color_bank))
        tim.fd(50)
    y += 50

#TODO: 1. work on color, change colormode

#TODO: 2.Work on removing a line






screen = turtle_modules.Screen()
screen.exitonclick()





#TODO: 8. Verify the code, optimize it.