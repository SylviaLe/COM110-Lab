
from graphics import *

def main():
    win = GraphWin("Image Processing", 800, 600)

    flowers = Image(Point(200,300), "pink.gif")
    flowers.draw(win)

    noFlowers = Image(Point(600,300), flowers.getWidth(), flowers.getHeight())
    noFlowers.draw(win)

    for x in range(int(flowers.getWidth())-1):
        for y in range(int(flowers.getHeight())-1):
            r, g, b = flowers.getPixel(x, y)
            r0, g0, b0 = flowers.getPixel(x+1, y+1)
            if abs(r-r0)>60 or abs(g-g0)>60 or abs(b-b0)>60:
                noFlowers.setPixel(x, y, color_rgb(r, g, b))
    noFlowers.save("No pink.gif")

    #Wait for a mouse click before closing win
    win.getMouse()
    win.close()

main()
