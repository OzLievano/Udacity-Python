import turtle

lengths = [15, 25, 35, 45, 55, 65, 75, 80, 90, 100]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)
