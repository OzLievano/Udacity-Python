#import turtle
import turtle
#Create object for Turtle
mary = turtle.Turtle()
#create object for color
color = "purple"
mary.color(color)
#create object for forward & right
distance = 100
angle = 72
#create object for list
sides = [1,2,3,4,5]

#create loop

for side in sides:
    mary.forward(distance)
    mary.right(angle)
