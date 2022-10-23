import turtle
u = int(input())
turtle.shape('turtle')
n = u
x = 1
k = 180-(180/n)
while x <= n:
    turtle.left(k)
    turtle.forward(100)
    x -= n
    
    
   