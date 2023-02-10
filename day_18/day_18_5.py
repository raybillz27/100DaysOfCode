from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"score: {self.score} High score {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
        # self.goto(0, 0)
        # self.write("GAME OVER!", align=ALIGN, font=FONT)

    # def highest_score(self):
    #     self.goto(0, 270)
    #     self.write(f"Highest score {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()








