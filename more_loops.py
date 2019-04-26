import turtle
amy = turtle.Turtle()
colors = ["red","orange","yellow"]
# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(110)
amy.pendown()

# Draw three red lines, with space in between

for color in colors:
    amy.color(color)
    amy.forward(50)
    amy.penup()
    amy.forward(25)
    amy.pendown()
