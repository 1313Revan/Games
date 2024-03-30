import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600, startx=975, starty=500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game loop
play_game = True
while play_game:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increment_score()

    # wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.score_reset()
        snake.snake_reset()

    # tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.score_reset()
            snake.snake_reset()

scoreboard.reset()

screen.exitonclick()
