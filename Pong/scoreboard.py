from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-75, 200)
        self.write(self.p1_score, align="center", font=("Courier", 75, "normal"))
        self.goto(75, 200)
        self.write(self.p2_score, align="center", font=("Courier", 75, "normal"))

    def p1_point(self):
        self.p1_score += 1
        self.update()

    def p2_point(self):
        self.p2_score += 1
        self.update()
