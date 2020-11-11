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

def main():
    #print an introduction
    print("This program creates a graph of a 10-year investment, accounting for growth.")
    
    #get principle and interest rate(apr)
    principle = float(input("Enter the initial amount of money: "))
    apr = float(input("Enter your interest rate (annual) in decimal: "))

    # Create window with 320x240 resolution for readability and usability
    # Add the title of Investment Growth Chart
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), " 0.0k").draw(win)
    Text(Point(20, 180), " 2.5k").draw(win)
    Text(Point(20, 130), " 5.0k").draw(win)
    Text(Point(20, 80), " 7.5k").draw(win)
    Text(Point(20, 30), " 10.0k").draw(win)

    # bar at 0 years (initial investment) (by multiplying px per $ of 0.02 by the investment)
    height = principle * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Subsequent years using for loop through years
    for year in range (1, 11):
        # Calculations
        principle = principle * (1 + apr)
        #draw result into graph
        x11 = year * 25 + 40
        height = principle * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # Exit conditions
    input("Press <Enter> to quit")
    win.close()

main()
