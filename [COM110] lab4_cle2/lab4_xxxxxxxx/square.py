from graphics import *
from time import *
from random import randrange

def drawpt(x,y,color,window):
    pt=Point(x,y)
    pt.setFill(color)
    pt.draw(window)
    
 
def main():
 
    win=GraphWin("Fun!", 400,600)

    color = color_rgb(76,0, 153)

    for x in range(201, 301):
        for y in range(201, 301):
            drawpt(x, y, color, win)

            pt = Point(x,y)
            pt.setFill(color)
            pt.draw(win)
        

    win.getMouse()
    win.close()
main()
