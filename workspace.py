import turtle

def square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)

def draw_flower(some_turtle):
    for petal in range(6):
        square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle

draw_flower(romeo)
