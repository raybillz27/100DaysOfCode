import turtle as t
from day_16_7 import color_list
import random
t.penup()
t.hideturtle()

t.colormode(255)
t.setheading(225)

t.forward(300)
t.setheading(0)
number_of_dot = 100

for number_count in range(1, number_of_dot + 1):
    t.speed("fastest")
    t.dot(20, random.choice(color_list))

    t.forward(50)

    if number_count% 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = t.Screen()
screen.exitonclick()
