from graphics import *
from time import *
from random import *

def drawButton(pt1,pt2,color,labelText,window):
    button=Rectangle(pt1,pt2)
    button.setFill(color)
    button.draw(window)

    centerX = (pt1.getX()+pt2.getX())/2
    centerY = (pt1.getY()+pt2.getY())/2
    
    #Put label on button
    label = Text(Point(centerX,centerY),labelText)
    label.setFill("white")
    label.draw(window)

def smush(string):
    newString = ""
    for char in string:
        if char >= "a" and char <= "z":
            newString += char
        elif char >= "A" and char <= "Z":
            newChar = char.lower()
            newString += newChar
    return newString

def reverse(string):
    newString = ""
    for char in string:
        newString = char + newString
    return newString

def isPalin(string):
    original = smush(string)
    new = reverse(original)
    if original == new:
        return True
    else:
        return False
    
def main():
    win = GraphWin("Window", 600, 600)
    win.setCoords(0, 0, 600, 600)

    drawButton(Point(400, 400), Point(500, 450), "blue3", "Lower Case", win)
    drawButton(Point(80, 400), Point(180, 450), "red3", "Smush", win)
    drawButton(Point(250, 400), Point(350, 450), "yellow3", "Reverse", win)
    drawButton(Point(250, 500), Point(350, 550), "purple3", "Palindrome", win)

    inputBox = Entry(Point(300, 350), 50)
    inputBox.draw(win)
    pt = win.getMouse()
    text = inputBox.getText()


    if pt.getX() >= 400 and pt.getX() <= 500 and pt.getY() >= 400 and pt.getY() <=450:
        newText = text.lower()
        output = Text(Point(300, 300), newText)
        output.draw(win)
        
    if pt.getX() >= 80 and pt.getX() <= 180 and pt.getY() >= 400 and pt.getY() <= 450:
        output2 = Text(Point(300, 300), smush(text))
        output2.draw(win)

    if pt.getX() >= 250 and pt.getX() <= 350 and pt.getY() >= 400 and pt.getY() <= 450:
        output3 = Text(Point(300, 300), reverse(text))
        output3.draw(win)

    if pt.getX() >= 250 and pt.getX() <= 350 and pt.getY() >= 500 and pt.getY() <= 550:
        if isPalin(text):
            output4 = Text(Point(300, 300), "The text you entered is a palindrome")
            output4.draw(win)
            while True:
                moveX = randrange(60)
                moveY = randrange(60)
                output4.move(moveX, moveY)

                r = randrange(256)
                g = randrange(256)
                b = randrange(256)
                color = color_rgb(r, g, b)


                output4.setTextColor(color)
                
                sleep(0.5)
                if win.checkMouse(): break
            
        else:
            output4 = Text(Point(300, 300), "The text you entered is not a palindrome")
            output4.draw(win)
        
    win.getMouse()
    win.close()
main()
