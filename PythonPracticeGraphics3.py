# PythonPracticeGraphics.py
# To try interatcive graphics with Python

# Import graphics.py

from graphics import *

# Create a clickable box
def main():
    win = GraphWin("Click Here!")
    # For loop that will report where a click occurs
    for i in range(10):
        p = win.getMouse()
        print("Click at: ", p.getX(), p.getX())

main()

