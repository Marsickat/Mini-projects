import turtle
import random


def draw_snowflake(x, y):
    turtle.speed(0)
    turtle.width(random.randint(1, 5))
    turtle.pencolor(random.randrange(256), random.randrange(256), random.randrange(256))
    step = random.randint(5, 20)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(8):
        for _ in range(3):
            turtle.forward(step)
            turtle.left(45)
            turtle.forward(step)
            turtle.backward(step)
            turtle.right(90)
            turtle.forward(step)
            turtle.backward(step)
            turtle.left(45)
        turtle.forward(step)
        turtle.backward(step * 4)
        turtle.left(45)


def left_mouse_click(x, y):
    draw_snowflake(x, y)


turtle.Screen().colormode(255)
turtle.Screen().bgcolor("cyan")
turtle.hideturtle()
turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()
turtle.mainloop()
