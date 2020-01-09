#lab 4 sunset of over house animation

from graphics import *
from time import *
from random import *


def main():

    window = GraphWin("House", 600, 600)
    #green lawn
    lawn = Rectangle(Point(0,620),Point(620,300))
    lawn.setFill("green4")
    lawn.draw(window)
    #blue-ish sky
    sky = Rectangle(Point(620,300),Point(0,0))
    sky.setFill(color_rgb(180,180,245))
    sky.draw(window)
    #red roof
    roof = Polygon(Point(200,200), Point(300,100),Point(400,200))
    roof.setFill("red3")
    roof.draw(window)
    #yellow house
    walls = Rectangle(Point(210,400),Point(390,200))
    walls.setFill("yellow2")
    walls.draw(window)
    #red door
    door = Rectangle(Point(280, 400),Point(320,320))
    door.setFill("red1")
    door.draw(window)
    #with doorknob
    doorknob = Circle(Point(315, 360),2)
    doorknob.draw(window)
    #two blue windows
    housewin1 = Rectangle(Point(320,300),Point(360, 250))
    housewin1.setFill("blue")
    housewin1.draw(window)
    housewin2 = Rectangle(Point(240,300),Point(280, 250))
    housewin2.setFill("blue")
    housewin2.draw(window)
    #yellow sun
    sun = Circle(Point(500,100),60)
    sun.setFill("yellow")
    sun.draw(window)
    window.getMouse()
    
    #animate sunset
    for i in range(35):
        sun.move(5,5) #move 5 pixels down and 5 pixels over at at ime
        #start from the initial blue-ish (color_rgb(180, 180, 247)) color (set above)
        sky.setFill(color_rgb(180-5*i,180-5*i,245-7*i)) #and fade down to color_rgb(0,0,0)
        sleep(.1) #slow the animation down so it looks good
        
    #after sunset, create stars
    star = [] #start with an empty list of stars
    for i in range(100):
        #generate random x and y values for a Point object
        xval = randrange(0,600) #random x spanning entire width of window
        yval = randrange(0,300) #random y going down to only top of lawn
        
        #make sure the location of the star is not inside the house
        while (insideHouse(xval,yval)): #if it's inside the house
            #try again, get new values
            xval = randrange(0,600) #random x spanning entire width of window
            yval = randrange(0,300) #random y going down to only top of lawn
            
        #here, because while loop ended, (xval,yval) must be a point outside the house
            
        star.append(Point(xval,yval)) #add Point to star list
        star[i].setFill("white")
        star[i].draw(window)


    #have each of the stars twinkle
    for i in range(10):
        for j in range(len(star)):
            star[j].undraw()
            sleep(.02)
            star[j].draw(window)
    
    #pause and wait for mouse click before closing window
    window.getMouse()
    window.close()


#returns True if the point (x,y) is inside the house, False otherwise
def insideHouse(x, y):
    #if enclosed within the three lines that form the roof
    if (y >= -x +400) and (y >= x - 200) and (y <= 200):
        underRoof = True
    else:
        underRoof = False
    #if enclosed within the four lines that form the house "walls"
    if x >= 210 and y >= 200 and y <= 400 and x <= 390:
        withinWalls = True
    else:
        withinWalls = False
    return (underRoof or withinWalls)


main()
