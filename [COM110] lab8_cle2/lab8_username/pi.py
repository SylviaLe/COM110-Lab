
from random import random
from graphics import *

def main():
    win = GraphWin("Dart Throw Simulator", 600, 600)
    win.setCoords(-3,-3,3,3)

    
    prompt = Text(Point(0, 2.5), "How many darts to throw?: ")
    prompt.draw(win)
    userInput = Entry(Point(0, 2), 8)
    userInput.draw(win)
    

    board = Rectangle(Point(-1,-1), Point(1, 1))
    board.setFill('white')
    board.draw(win)

    win.getMouse()
    throws = int(userInput.getText())

    count = 0
    for i in range(throws):
        x = random() * 2 - 1
        y = random() * 2 - 1
        pt = Point(x, y)
        if x**2 + y**2 <= 1:
            count += 1
            pt.setFill("green")
            pt.draw(win)
        else:
            pt.setFill("red")
            pt.draw(win)
            
    pi = ((count/throws)*4)
    piString = "The approx. pi is: " + str(pi)
    dartString = str(count) + " darts fall into the circle"
        
    dartsIn = Text(Point(0, -1.75), dartString)
    dartsIn.draw(win)
    pivalue = Text(Point(0, -2), piString)
    pivalue.draw(win)

    win.getMouse()
    win.close()
main()
