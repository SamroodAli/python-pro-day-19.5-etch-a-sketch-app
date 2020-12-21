from turtle import Turtle, Screen, onkey

t = Turtle()
scr = Screen()
scr.listen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_clockwise():
    t.right(10)


def turn_counter_clockwise():
    t.left(10)


onkey(key='w', fun=move_forward)
onkey(key='a', fun=turn_counter_clockwise)
onkey(key='s', fun=move_backward)
onkey(key='d', fun=turn_clockwise)
scr.exitonclick()
