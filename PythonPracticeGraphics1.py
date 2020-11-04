# Programme to practice simple graphical integration with python

from graphics import *

win = GraphWin()

# Draw a red circle at 100, 100 with a radius of 30
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

# Addition of text to circle
label = Text(center, "Red Circle")
label.draw(win)

# Add a clear rectangle to image
rect = Rectangle(Point(20, 30), Point(70, 70))
rect.draw(win)

win.getMouse()
win.close()
