# A library for generating random x and y coordinates 
# and storing them in a csv file (Unordered) 

import csv
import random
# generates coordinates with no of points(numPoints) as input
def generateCoordinates(numPoints):
    coordinates = []
    for _ in range(numPoints):
        x = random.randint(0, 90)
        y = random.randint(0, 60)
        coordinates.append((x, y))
        # saving in form of tuple
    return coordinates

# saves the unordered coordinates to a file
def saveToCsv(coordinates, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['x', 'y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #using Dictwriter to write to csvfile
        writer.writeheader()
        for coord in coordinates:
            writer.writerow({'x': coord[0], 'y': coord[1]})

