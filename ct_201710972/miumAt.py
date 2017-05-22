import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def giyukAt(x,y,size):  
    t1.goto(x,y)
    t1.lt(90)  
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)

def niunAt(size):    
    t1.lt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)

def miumAt(x,y,size):
    t1.goto(x,y)
    giyukAt(x,y,size)
    niunAt(size)


miumAt(-100,100,200)