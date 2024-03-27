from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.movement_speed = 0.08
        self.x_trajectory = 10
        self.y_trajectory = 10

    def move(self):
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.hideturtle()
        self.goto(0, 0)
        self.movement_speed = 0.1
        self.showturtle()
        self.x_bounce()

    def y_bounce(self):
        self.y_trajectory *= -1

    def x_bounce(self):
        self.x_trajectory *= -1
        self.movement_speed *= 0.9
