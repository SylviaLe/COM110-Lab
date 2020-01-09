from graphics import *
from time import sleep
def main():
    win = GraphWin("Picture of a house", 800, 600)
    win.setCoords(0, 0, 800, 800)

    grass = Rectangle(Point(0, 0), Point(800, 150))
    grass.setFill("green")
    grass.setOutline("green")
    grass.draw(win)

    sun = Circle(Point(700, 570), 50)
    sun.setFill("orange")
    sun.setOutline("orange")
    sun.draw(win)

    base = Rectangle(Point(250, 120), Point(500,300))
    base.setFill("blanched almond")
    base.setOutline("blanched almond")
    base.draw(win)

    roof = Polygon(Point(190, 300), Point(560, 300), Point(375, 700))
    roof.setFill("indian red")
    roof.setOutline("indian red")
    roof. draw(win)

    door = Rectangle(Point(320, 120), Point(370, 220))
    door.setFill("light salmon")
    door.setOutline("light salmon")
    door.draw(win)

    window = Rectangle(Point(420, 170), Point(470, 220))
    window.setFill('MistyRose2')
    window.setOutline('MistyRose2')
    window.draw(win)

    win.setBackground(color_rgb(174, 253, 255))
    for i in range(35):
        sun.move(5, 5)
        sleep(0.02)
        color = color_rgb(180 - 5*i, 180 - 5*i, 245 - 7*i)
        win.setBackground(color)
        
    
    win.getMouse()
    win.close()

main()
