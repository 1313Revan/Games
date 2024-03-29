import time
from turtle import Screen

from player import Player, START_POS, FINISH_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600, startx=950, starty=350)
screen.title("Turtle Crossing")
screen.bgcolor("DarkGrey")
screen.tracer(0)

# Objects
player = Player()
score = Scoreboard()
cars = CarManager()

# Player Movement
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

# Game Loop
play_game = True
while play_game:
    time.sleep(0.1)
    screen.update()
    score.update_score()
    cars.create_car()
    cars.move_car()

    # Detect Player/Car Locations
    for car in cars.all_cars:
        car_y = car.ycor()
        car_x = car.xcor()
        player_y = player.ycor()
        player_x = player.xcor()
        abs_y = abs(car_y - player_y)
        abs_x = abs(car_x - player_x)
        # Player Hit?
        if abs_y < 18 and abs_x <= 20:
            score.game_over()
            play_game = False

    # Next Level
    if player.ycor() > FINISH_Y:
        player.goto(START_POS)
        score.increase_score()
        cars.increase_speed()

screen.exitonclick()
