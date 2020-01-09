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

    alert = Text(Point(200, 200), "")
    alert.draw(win)

    pt = win.getMouse()
    haveResult = False
    while (not quitButton.isClicked(pt)):
        if rollDice.isClicked(pt):
            quitButton.activate()

            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)

            iniRoll = value1 + value2
            if iniRoll == 2 or iniRoll == 3 or iniRoll == 12:
                alert.setText('YOU LOSE!!')
                haveResult = True
                rollDice.deactivate()
            elif iniRoll == 7 or iniRoll == 11:
                haveResult = True
                alert.setText('YOU WIN!!')
                rollDice.deactivate()
            else:
                pt = win.getMouse()
                if rollDice.isClicked(pt):
                    value1 = randrange(1, 7)
                    die1.setValue(value1)
                    value2 = randrange(1, 7)
                    die2.setValue(value2)

                    if value1 + value2 == iniRoll:
                        alert.setText('YOU WIN!!')
                        haveResult = True
                        rollDice.deactivate()
                    if value1 + value2 == 7:
                        alert.setText('YOU LOSE!!')
                        haveResult = True
                        rollDice.deactivate()


        pt = win.getMouse()

    win.close()

main()
