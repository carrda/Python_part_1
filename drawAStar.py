# Draw a star with Turtle Graphics

from turtle import *

for i in range(5):
    forward(100)
    right(144)

up()
forward(200)
down()

for i in range(5):
    forward(50)
    right(144)

up()
right(90)
forward(150)
down()

pencolor('orange')
width(10)
circle(180)

mainloop()