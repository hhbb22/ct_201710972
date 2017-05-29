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


def drawTriangleAt(x,y,size):
      t1.penup()
      t1.goto(x,y)
      t1.pendown()

      for i in range(0,3):
          t1.forward(size)
          t1.write(t1.pos())
          t1.left(120)
          
                  
def drawPentagon(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
     

    for i in range(0,5):
         t1.fd(size)
         t1.write(t1.pos())
         t1.lt(72)


def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    

    for i in range(0,5):
        t1.fd(size)
        t1.write(t1.pos())
        t1.rt(144)




drawTriangleAt(-100,100,100)


drawPentagon(-300,100,100)


drawStarAt(-450,100,100)




    


    
