import turtle

t = turtle.Turtle()

t.shape("turtle")

t.color('red')
t.pensize(5)

for x in range(10):
    t.forward(300)
    t.left(90)


