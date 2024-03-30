from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\tHigh Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()
