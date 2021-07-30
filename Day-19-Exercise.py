import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.forward(20)


screen.listen()
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()
