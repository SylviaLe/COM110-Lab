from dieview import DieView
from button import Button
from graphics import *
from random import randrange

def main():
    win = GraphWin("Die View", 400, 400)
    win.setBackground('lavender')
    win.setCoords(0, 0, 400, 400)

    rollDice = Button(win, Point(200, 150), 100, 40, 'Roll Dice')
    rollDice.activate()
    quitButton = Button(win, Point(200, 100), 50, 25, 'Quit')
    quitButton.deactivate()

    die1 = DieView(win, Point(100, 300), 50)
    die2 = DieView(win, Point(300, 300), 50)

    pt = win.getMouse()
    while not quitButton.isClicked(pt):
        if rollDice.isClicked(pt):
            quitButton.activate()
            die1.setValue(randrange(1, 7))
            die2.setValue(randrange(1, 7))
        pt = win.getMouse()

    win.close()

main()
