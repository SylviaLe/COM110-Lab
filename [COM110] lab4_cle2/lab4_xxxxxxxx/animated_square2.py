
from graphics import *
from time import *
from random import randrange

def drawpt(x,y,color,window):
    pt=Point(x,y)
    pt.setFill(color)
    pt.draw(window)
    sleep(0.0001)
 
def main():
 
    win=GraphWin("Fun!", 400,600)

    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    color = color_rgb(r,g,b)

    for y in range(100, 110):
        for x in range(100,301):
            drawpt(x,y,color,win)

            pt=Point(x,y)
            pt.setFill(color)
            pt.draw(win)

    #square=Rectangle(Point(100,100),Point(300,300))
    #square.setFill("teal")
    #square.draw(win)

 
    sendoff = Text(Point(200,400),"Click anywhere to close.")
    sendoff.draw(win)
    win.getMouse()
    win.close()
   
main()
