from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("black")
        self.goto(x=-225, y=265)
        self.level = 1

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
