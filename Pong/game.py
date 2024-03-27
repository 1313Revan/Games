# Here is an endless game of Pong
# Made alongside Angela Yu in her Python bootcamp

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=875, starty=350)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game = True
while game:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # paddle bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # left player scores
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.p1_point()

    # right player scores
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.p2_point()

screen.exitonclick()
