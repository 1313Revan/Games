from turtle import Turtle, Screen

# W = Forward
# A = Counter-Clockwise
# S = Backward
# D = Clockwise
#
# C = Clear Drawing, Move to Home

pen = Turtle()
screen = Screen()
screen.setup(2048, 1152, 100, 100)

def move_fd():
    pen.fd(10)
def move_bk():
    pen.bk(10)
def turn_rt():
    pen.right(10)
def turn_lf():
    pen.left(10)
def clear():
    pen.clear()
    pen.pu()
    pen.home()
    pen.pd()

screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=turn_lf)
screen.onkey(key="d", fun=turn_rt)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
