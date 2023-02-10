from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)
        self.paddle_move_up = 20
        self.paddle_move_down = 20

    def go_up(self):
        new_y = self.ycor() + self.paddle_move_up
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - self.paddle_move_down
        self.goto(self.xcor(), new_y)





    



