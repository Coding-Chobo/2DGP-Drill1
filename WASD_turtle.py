import turtle
turtle.shape('turtle')
def move(x):
    if x == 'w':
        turtle.setheading(90)
        turtle.forward(50)
    elif x == 's':
        turtle.setheading(270)
        turtle.forward(50)
    elif x == 'a':
        turtle.setheading(180)
        turtle.forward(50)
    elif x == 'd':
        turtle.setheading(0)
        turtle.forward(50)

turtle.onkey(lambda: move('w'), 'w')
turtle.onkey(lambda: move('a'), 'a')
turtle.onkey(lambda: move('s'), 's')
turtle.onkey(lambda: move('d'), 'd')
turtle.listen()

turtle.exitonclick()