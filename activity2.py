import turtle

screen = turtle.Screen()
screen.title("I am very happy :)")
screen.bgcolor("Lime")
screen.setup(600, 600)
t = turtle.Turtle()
t.pensize(7)
t.color("White")

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.left(90)
t.penup()
t.forward(100)
t.right(90)
t.pendown()

t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)


turtle.done()