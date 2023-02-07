from turtle import Turtle, Screen
from day_19_3 import Paddle
from day_19_4 import Ball
import time

screen = Screen()
paddle = Turtle()
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
    # detect l_paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()





screen.exitonclick()