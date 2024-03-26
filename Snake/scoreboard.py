from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score()
