from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")

def move_forward():
    global tim
    tim.forward(10)

def move_backward():
    global tim
    tim.backward(10)

def clock():
    global tim
    tim.right(10)

def counter_clock():
    global tim
    tim.left(10)

def clear():
    global tim
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(clock, "d")
screen.onkeypress(counter_clock, "a")
screen.onkeypress(clear, "c")
screen.exitonclick()