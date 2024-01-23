from turtle import Turtle, Screen

joe = Turtle()
screen = Screen()


def turn_left():
    joe.left(5)


def turn_right():
    joe.right(5)


def move():
    joe.forward(10)


def move_backwards():
    joe.forward(-10)


def clean():
    joe.clear()
    joe.setheading(0)
    joe.teleport(0, 0)


screen.listen()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clean, "c")




screen.exitonclick()