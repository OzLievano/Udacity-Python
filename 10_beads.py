import turtle

def bead(tur)
    tur.right(45)
    for n in range(12):
        tur.forward(10)
        turn.left(30)

t = turtle.Turtle()
t.speed(0)
t.width(5)

#Move the the Left before starting
t.penup()
t.back(200)
t.pendown()
#Draw 10 beads
    for n in range(10):
        if n % 2 == 0:
            t.color("blue")
        else:
            t.color("red")
        bead(t)
        t.forward(40)
