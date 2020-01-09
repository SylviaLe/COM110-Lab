
from graphics import *
from math import sqrt
from random import randrange

#Calculates and resturns the distance between pt1 and pt2
def distance(pt1,pt2):
    x1 = pt1.getX()
    y1 = pt1.getY()
    x2 = pt2.getX()
    y2 = pt2.getY()

    dist = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return dist
#extract letter from text
def extract(text):
    newText = ""
    for char in text:
        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            newText += char
    return newText

def drawCircle(center,radius,color,window):
    circ = Circle(center,radius)
    circ.setFill(color)
    circ.draw(window)

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

def main():
    
    win=GraphWin("Button GUI", 800,800)

    win.setCoords( 0,0, 100,100)

    drawButton(Point(5,96), Point(15,90),"blue3","OUT",win)
    
    drawButton(Point(25,96), Point(35,90),"blue3","Circle",win)
    
    drawButton(Point(55,96), Point(65,90),"red","Square",win)

    drawButton(Point(75,96), Point(85,90),"red","Concentric",win)

    win.getMouse()
    

    pt=win.getMouse()

    while not(pt.getX()>=5 and pt.getX()<=15 and pt.getY()>=90 and pt.getY()<=96):
    #the .getX() function returns the x-value of a Point object
        if pt.getX()>=25 and pt.getX()<=35 and pt.getY()>=90 and pt.getY()<=96: 
            drawCircle(Point(50,50),20,'red',win)


        elif pt.getX()>=55 and pt.getX()<=65 and pt.getY()>=90 and pt.getY()<=96:
            square = Rectangle(Point(60,60),Point(70,70))
            square.setFill("yellow")
            square.draw(win)


        elif pt.getX()>=75 and pt.getX()<=85 and pt.getY()>=90 and pt.getY()<=96:
            message = Text(Point(50, 80), "Enter the number of circle you want to draw")
            message.draw(win)

            userInput = Entry(Point(50, 70), 50)
            userInput.draw(win)
            win.getMouse()

            number = eval(userInput.getText())
            i = 0
            radius = 10
            while i < number:
                r = randrange(256)
                g = randrange(256)
                b = randrange(256)
                color = color_rgb(r,g,b)
                drawCircle(Point(50, 50), radius, color, win)
                radius += -2
                i = i + 1
                

        else:
            pt.draw(win)
        pt=win.getMouse()
        
    closeMessage = Text(Point(50,5), "Click anywhere to end program.")
    closeMessage.draw(win)
    
    win.close()


main()

