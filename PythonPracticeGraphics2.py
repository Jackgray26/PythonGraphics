# Code to calculate the growth of an investment over 10 years, with a graphical output

from graphics import * 

# Y Axis labels up to 10 Thousand
# starting at 10 px up from bottom and 20 in

#Draw label " 0.0K" at (20, 230)
#Draw Label " 2.5K" at (20, 180)
#Draw Label " 5.0K" at (20, 130)
#Draw Label " 275K" at (20, 80)
#Draw Label " 10.0K" at (20, 30)

# Note: 100 px is $5,000 or 0.02 px per $
# each bar can be 25 px to account for margins

def drawBar(window, year, height):
    # Draws a bar using given values
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    #print an introduction
    print("This program creates a graph of a 10-year investment, accounting for growth.")
    
    #get principle and interest rate(apr)
    principle = float(input("Enter the initial amount of money: "))
    apr = float(input("Enter your interest rate (annual) in decimal: "))

    # Create window with 320x240 resolution for readability and usability
    # Add the title of Investment Growth Chart
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setCoords(-1.75, 2000, 11.5, 10400.0)
    win.setBackground("white")
    
    Text(Point(-1, 0), " 0.0k").draw(win)
    Text(Point(-1, 2500), " 2.5k").draw(win)
    Text(Point(-1, 5000), " 5.0k").draw(win)
    Text(Point(-1, 7500), " 7.5k").draw(win)
    Text(Point(-1, 10000), " 10.0k").draw(win)

    # draw the bar using drawBar
    drawBar(win, 0, principle)
    for year in range(1, 11):
        principle = principle * (1 + apr)
        drawBar(win, year, principle)

    # Exit conditions
    input("Press <Enter> to quit")
    win.close()

main()
