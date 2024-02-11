# A library for arranging the coordinates in increasing order .

import csv
#error handling of string fieldnames 
def toFloat(a):
    try:
        return float(a)
    except ValueError:
        return 0

def sortCoordCsv(inpFile, outFile):
    # Read the input CSV file
    with open(inpFile, 'r') as file:
        reader = csv.reader(file)
        coordinates = list(reader)
      

 # Sort the coordinates based on x and then y
 # Sorted on the basis of x coordinate first and y second 
    coordinates.sort(key=lambda x: (toFloat(x[0]), toFloat(x[1])))    # using lambda to iterate each row 

    # Writing the sorted coordinates to a new CSV file
    with open(outFile, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(coordinates)
