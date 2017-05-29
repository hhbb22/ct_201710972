import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

    
win = turtle.Screen()
width = win.window_width()
w3 = (width - 40) / 3

x1 = 0.0 - w3
x2 = 0.
x3 = 0. + w3


t1.penup()
t1.goto(x1, 0)
t1.pendown()
t1.pos()
t1.write(t1.pos())

t1.clear()


def drawTriangleAt():
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)

        

def drawPentagon():
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)


def drawStarAt():
    t1.fd(100)
    t1.write(t1.pos())
    t1.rt(144)
    t1.fd(100)
    t1.write(t1.pos())
    t1.rt(144)
    t1.fd(100)
    t1.write(t1.pos())
    t1.rt(144)
    t1.fd(100)
    t1.write(t1.pos())
    t1.rt(144)
    t1.fd(100)
    t1.write(t1.pos())
    t1.rt(144)




drawTriangleAt()

t1.reset()

t1.penup()
t1.goto(x1, 0)
t1.pendown()
t1.pos()
t1.write(t1.pos())

t1.clear()


drawPentagon()

t1.penup()
t1.goto(x1, 0)
t1.pendown()
t1.pos()
t1.write(t1.pos())

t1.clear()


t1.reset()

t1.penup()
t1.goto(x1, 0)
t1.pendown()
t1.pos()
t1.write(t1.pos())

t1.clear()


drawStarAt()




    


    
