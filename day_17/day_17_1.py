# turtle

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def anti_clock_wise():
    t.left(19)


def clock_wise():
    t.right(10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
