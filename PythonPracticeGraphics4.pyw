# Python Practice Graphics 4
# Working to create a triangle based on user input

# Import from graphics.py
from graphics import *

def main():

    win = GraphWin("Click to place the points of a triangle.")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click in three Locations")
    message.draw(win)

    
