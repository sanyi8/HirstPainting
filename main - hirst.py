import turtle
from turtle import Turtle
import random

color_list = [(224, 228, 233), (234, 229, 232), (132, 168, 203), (193, 164, 142), (62, 89, 139), (120, 78, 99),
              (184, 152, 172), (158, 75, 47), (54, 119, 94), (220, 230, 85), (137, 191, 151), (45, 52, 106),
              (113, 116, 184), (36, 44, 62), (226, 134, 14), (175, 187, 214), (176, 95, 115), (90, 47, 62),
              (213, 181, 194), (35, 29, 28), (41, 49, 45), (56, 41, 51), (109, 168, 71), (111, 39, 36),
              (224, 79, 40), (233, 174, 157), (165, 208, 176), (23, 98, 79)]

# generate random color from list
random_color = random.choice(color_list)

t = Turtle()
# 10 x 10 size, 20 dot_size, 50 step
dot_size = 30
step = 60
x_axle = 10
y_axle = 10

# screen mode setup
screen = turtle.Screen()
screen.colormode(255)   # allow to use RGB 0-255 otherwise only 0-1

# setup turtle steps
t.penup()
t.speed(0)
# t.color("white")
t.hideturtle()

# store and set turtle staring position
start_position = (-300, -200)
t.goto(start_position)

for y in range(y_axle):
    for x in range(x_axle):
        random_color = random.choice(color_list)
        t.dot(dot_size, random_color)
        t.penup()
        t.forward(step)

    # after each line
    t.goto(start_position[0], start_position[1] + (y+1) * step)
    t.setx(start_position[0]) # will keep x position the same

# screen setup

turtle.exitonclick()

