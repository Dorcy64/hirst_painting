import random
from turtle import Turtle, Screen

# This code will draw a 10 by 10 table with random colors in this list of rgb generated from colorgram
# The colorgram image used is in this file directory

color_scheme = [(207, 167, 99), (196, 220, 236), (226, 208, 113), (202, 137, 154), (128, 164, 196), (45, 105, 166),
                 (231, 217, 227), (230, 217, 188), (147, 67, 97), (136, 189, 169), (191, 85, 100), (152, 212, 193),
                 (189, 221, 207), (168, 150, 56), (147, 97, 61), (86, 126, 182), (199, 91, 82), (223, 171, 182),
                 (126, 32, 71), (21, 57, 124)]

# This will turn the screen to rgb colormode so we can pass in the rgb list

screen = Screen()
screen.colormode(255)

# This will remove the pen from the canvas and hide the turtle as we draw
tim = Turtle()
tim.penup()
tim.shape("circle")
tim.goto(-250, -250)
tim.speed(5)
tim.hideturtle()

# This is the  y-coordinate where the code will start from when done with 10 circles in a row
place = -200

for _ in range(10):
    # This will draw 10 dots in a row, colored with random colors from the colorscheme list
    for _ in range(10):
        x = random.choice(color_scheme)
        tim.pendown()
        tim.dot(20, x)
        tim.penup()
        tim.forward(50)

    # This will take the turtle to the same x coordinate as the other but different y-coordinate
    tim.goto(-250, place)
    place += 50

# This will help us not exit the screen when done
screen.exitonclick()
