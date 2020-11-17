# Graphics program to capture and display user inputted text in a textbox

# Converts Celsius to fahrenheit, within a graphical interface

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    
    # Interface Creation
    Text(Point(1, 3), "Celsius Temperature: ").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature: ").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")

    inputText.draw(win)
    outputText = Text(Point(2.25, 1), " ")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "CONVERT!")
    button.draw(win)
    Rectangle(Point(1.0, 1.5), Point(2, 2.5)).draw(win)