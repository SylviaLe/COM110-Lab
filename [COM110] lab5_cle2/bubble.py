from graphics import *
from random import randrange

def drawCircle(centre, radius, color, window):
    bubble = Circle(centre, radius)
    bubble.setFill(color)
    bubble.draw(window)

def main():
    win = GraphWin("Bubble", 500, 500)
    win.setCoords(0, 0, 50, 50)
    while True:
        centreX = randrange(50)
        centreY = randrange(50)
        radius = randrange(25)
        r = randrange(256)
        g = randrange(256)
        b = randrange(256)
        color = color_rgb(r, g, b)

        drawCircle(Point(centreX, centreY), radius, color, win)

        if win.checkMouse(): break        
main()
