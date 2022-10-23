import turtle,math
t=turtle
t.shape('turtle')
def prav_mu(R,rx,n):
    t.left(30) #zero angle
    n_obj=1
    n_edg=3
    a=2*R*math.sin(math.pi/n_edg)
    ang=360/n_edg
    while n_obj<n:
        ang_temp1=(n_edg-2)*180/n_edg
        a=2*R*math.sin(math.pi/n_edg)
        for i in range(n_edg):
            t.left(ang)
            t.forward(a)
        t.penup()
        t.goto(rx*n_obj,0)
        t.pendown()
        R+=rx
        n_edg+=1
        n_obj+=1
        ang=360/n_edg
        ang_temp2=(n_edg-2)*180/n_edg
        ang2=(ang_temp2-ang_temp1)/2
        t.left(ang2)
prav_mu(40,25,11)
t.done()