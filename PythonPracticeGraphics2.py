# Code to calculate the growth of an investment over 10 years, with a graphical output

from graphics import * 


# Create window with 320x240 resolution for readability and usability
# Add the title of Investment Growth Chartt

win = GraphWin("Investment Growth Chart", 320, 240)

# Y Axis labels up to 10 Thousand
# starting at 10 px up from bottom and 20 in

Draw label " 0.0K" at (20, 230)
Draw Label " 2.5K" at (20, 180)
Draw Label " 5.0K" at (20, 130)
Draw Label " 275K" at (20, 80)
Draw Label " 10.0K" at (20, 30)

# Note: 100 px is $5,000 or 0.02 px per $
# each bar can be 25 px to account for margins

def main():
    #print an introduction
    print("This program creates a graph of a 10-year investment, accounting for growth.")
    
    #get principle and interest rate
    



