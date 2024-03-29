from turtle import Turtle

START_POS = (0, -280)
FINISH_Y = 280

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("ForestGreen")
        self.pu()
        self.goto(START_POS)
        self.seth(UP)

    def move_up(self):
        self.seth(UP)
        new_pos = self.ycor() + 10
        self.goto(self.xcor(), new_pos)

    def move_down(self):
        self.seth(DOWN)
        if self.ycor() >= -270:
            new_pos = self.ycor() - 10
            self.goto(self.xcor(), new_pos)

    def move_left(self):
        self.seth(LEFT)
        if self.xcor() >= -270:
            new_pos = self.xcor() - 10
            self.goto(new_pos, self.ycor())

    def move_right(self):
        self.seth(RIGHT)
        if self.xcor() <= 270:
            new_pos = self.xcor() + 10
            self.goto(new_pos, self.ycor())
