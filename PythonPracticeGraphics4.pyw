# Python Practice Graphics 4
# Working to create a triangle based on user input

# Import from graphics.py
from graphics import *

def main():

    win = GraphWin("Click to place the points of a triangle.")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click in three Locations")
    message.draw(win)

    # Get and draw each point and line based on input

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)


    # fill the object via a polygon
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
