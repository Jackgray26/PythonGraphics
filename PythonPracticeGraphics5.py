# Graphics Program to use click-placable text with python

from graphics import *

def main():
    win =  GraphWin("Click to place Text", 400, 400)
    # for loop to take user input, and start drawing text
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

main()
