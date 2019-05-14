import turtle

jack= turtle.Turtle()


def draw_square(length,color):
    jack.color(color)
    for n in range(4):
        jack.forward(length)
        jack.right(90)

draw_square(20,"red")

jack.penup()
jack.back(150)
jack.pendown()

draw_square(25,"blue")
jack.forward(100)
draw_square(12,"orange")
jack.forward(100)
draw_square(54,"black")

for square in range(80):
    draw_square(20,"white")
    jack.forward(5)
    jack.left(5)
