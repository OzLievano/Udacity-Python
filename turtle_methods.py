#import turtle
import turtle

ozzy= turtle.Turtle()

#make the width thicker so that the line will be easier to see

ozzy.width(5)

#move back without drawing anything

ozzy.penup()
ozzy.back(100)

#Draw a red line

ozzy.pendown()
ozzy.color("red")
ozzy.forward(50)

#Move forward without drawing anything
ozzy.penup()
ozzy.forward(25)

#Draw a orange line
ozzy.pendown()
ozzy.color("orange")
ozzy.forward(50)

#Move forward without drawing anything
ozzy.penup()
ozzy.forward(25)

#draw a yellow line
ozzy.pendown()
ozzy.color("yellow")
ozzy.forward(50)
