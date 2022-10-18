import turtle

turtle.shape('turtle') 
a = 10 
while a > 1:
    turtle.pendown()
    for i in range(4):
        turtle.forward(a * 10)
        turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    a -= 2


