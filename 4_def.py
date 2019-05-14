import turtle

def spiral(sides,turn,color,width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(sides)
        t.right(turn)

spiral(100,45,"red",2)
