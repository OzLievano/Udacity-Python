import turtle

# Set the number of sides here.
sides = 8

# Set the length of a side here.
length = 80

t = turtle.Turtle()
t.color("orange")
t.back(50)
for side in range(sides):
    t.forward(length)
    t.right(360/sides)
    # On the line above, replace the
    # value 72 with an arithmetic
    # expression that uses the
    # 'sides' variable.
