import turtle

t = turtle.Turtle()
scr = turtle.Screen()
scr.listen()
scr.title("Etch a Sketch")


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_clockwise():
    t.right(10)


def turn_counter_clockwise():
    t.left(10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


turtle.onkey(key='w', fun=move_forward)
turtle.onkey(key='a', fun=turn_counter_clockwise)
turtle.onkey(key='s', fun=move_backward)
turtle.onkey(key='d', fun=turn_clockwise)
turtle.onkey(key='c', fun=clear_screen)
scr.exitonclick()
