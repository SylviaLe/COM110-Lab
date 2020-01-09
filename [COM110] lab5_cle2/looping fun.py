from graphics import *
from random import randrange

def drawSquare(pt1, pt2, color, window):
    square = Rectangle(pt1, pt2)
    square.setFill(color)
    square.draw(window)

def main():
    win = GraphWin("Looping Color", 500, 500)
    win.setCoords(0, 0, 10, 10)
    for row in range(10):
        for col in range(10):
            r = randrange(256)
            g = randrange(256)
            b = randrange(256)
            color = color_rgb(r,g,b)
            drawSquare(Point(row, col), Point(row + 1, col + 1), color, win)

    win.getMouse()
    win.close()
main()
            






   
