#Each number is meant to be treated as an angle
angles = [-90, 0, 0, -90,
          135, 0, 0, 0,
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

#Fill out the for loop. Keep the distance the same and change the angle.
#Have the turtle turn right by the number from the list (angles) and go forward by 25 pixels

#Your answer here

#import turtle
import turtle
#name turtle
ozzy = turtle.Turtle()
#use a color variable
color = ozzy.color("red")
#Write for loop

for angle in angles:
    ozzy.right(angle)
    ozzy.forward(25)
