
from graphics import *
from random import randrange

def main():
    win = GraphWin("Image Processing", 800, 600)

    flowers = Image(Point(200,300), "pink.gif")
    flowers.draw(win)

    noFlowers = Image(Point(600,300), flowers.getWidth(), flowers.getHeight())
    noFlowers.draw(win)

    for x in range(int(flowers.getWidth())):
        for y in range(int(flowers.getHeight())):
            r, g, b = flowers.getPixel(x, y)
            if (g > r) and (g > b):
                noFlowers.setPixel(x, y, color_rgb(r, g, b))
            else:
                r = randrange(130)
                g = randrange(100, 255)
                b = randrange(130)
                noFlowers.setPixel(x, y, color_rgb(r, g, b))
    noFlowers.save("No pink.gif")

    #Wait for a mouse click before closing win
    win.getMouse()
    win.close()

main()
