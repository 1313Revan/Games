from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400, startx=1000, starty=500)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []

y_coord = -75
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_coord)
    racers.append(new_turtle)
    y_coord += 30

user_bet = screen.textinput(title="Race Bet", prompt="Choose a turtle to bet on!").lower()

race = False
if user_bet:
    race = True

while race:
    for turtle in racers:
        if turtle.xcor() >= 220:
            race = False
            winner = turtle.pencolor()
            print(f"\nThe winner is {winner}!")
            if user_bet == winner:
                print("Your bet was the winner!\n")
            else:
                print("Sorry, your bet lost.\n")
        turtle.fd(randint(0, 10))

screen.exitonclick()
