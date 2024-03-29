#  main program 
from Lib1 import *
from Lib2 import *
import matplotlib.pyplot as pl
import pandas as pd
# generating random coordinates 
coordinates = generateCoordinates(100) # no of coordinates here 

# saving to a csv file 
saveToCsv(coordinates, 'coordinatesUn.csv')

# ordering the coordinates
sortCoordCsv('coordinatesUn.csv', 'coordinatesOr.csv')
# plotting the coordinates
def plotCoordinates(csvFile, gridInt):
    # Reading CSV file
    d = pd.read_csv(csvFile)

    # getting x and y coordinates here 
    x = d['x']
    y = d['y']

    # Creating plot
    pl.scatter(x, y)
    pl.xlabel('X')
    pl.ylabel('Y')
    pl.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Setting custom grid interval 
    pl.minorticks_on()
    pl.grid(which='minor', linestyle=':', linewidth='0.5', color='black', alpha=0.7, axis='both')
    pl.gca().set_xticks(range(int(min(x)), int(max(x)), gridInt))
    pl.gca().set_yticks(range(int(min(y)), int(max(y)), gridInt))

    # showing plot
    pl.show()

# Example usage:
csvFile = "coordinatesOr.csv"
# inputing grid interval by user 
gridInt = int(input("Enter grid interval size: "))
plotCoordinates(csvFile, gridInt)