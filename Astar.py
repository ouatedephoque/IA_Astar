__author__ = 'jeshon.assuncao & rey.tom'
from math import sqrt

connections = [] # Create our array of connections
positions = [] # Create our array of positions

def Astar(townA, townB):
    print("tg")

def h0(n):
    return 0

# Distance between n and B on X axis
def h1(n, B):
    startX = 0
    stopX = 0

    for pos in positions:
        if(pos["Town"] == n):
            startX = int(pos["X"])

        if(pos["Town"] == B):
            stopX = int(pos["X"])

    return abs(startX - stopX);

# Distance between n and B on Y axis
def h2(n, B):
    startY = 0
    stopY = 0

    for pos in positions:
        if(pos["Town"] == n):
            startY = int(pos["Y"])

        if(pos["Town"] == B):
            stopY = int(pos["Y"])

    return abs(startY - stopY);

# Radial distance between n and B
def h3(n, B):
    distX = h1(n,B)
    distY = h2(n,B)

    return  sqrt(distX*distX + distY*distY)

# Manhattan distance between n and B
def h4(n, B):
    return h1(n,B) + h2(n,B)

def parseConnection(file):
    for ligne in file.readlines():
        connection = {} # Create our dictionary of one connection
        position = {} # Create our dictionary of one connection

        i = 0
        for word in ligne.split(" "):
            word = word.replace('\n', '') # Delete the line return

            if(i==0):
                connection["A"] = word # Add the start town in our connection dictionary
            elif(i==1):
                connection["B"] = word # Add the stop town in our connection dictionary
            else:
                connection["Dist"] = word # Add the distance between the two town in our connection dictionary

            i += 1

        connections.append(connection) # Add our connection in our connections array

def parsePosition(file):
    for ligne in file.readlines():

        position = {} # Create our dictionary of one position

        i = 0
        for word in ligne.split(" "):
            word = word.replace('\n', '') # Delete the line return

            if(i==0):
                position["Town"] = word # Add the town in our position dictionary
            elif(i==1):
                position["X"] = word # Add the x position of the town in our position dictionary
            else:
                position["Y"] = word # Add the y position of the town in our position dictionary

            i += 1

        positions.append(position) # Add our connection in our connections array

if __name__ == "__main__":
    import sys

    connectionFile = open(sys.argv[1], 'r')
    positionFile = open(sys.argv[2], 'r')

    parseConnection(connectionFile)
    parsePosition(positionFile)

    print(h0("Hamburg"))
    print(h1("Hamburg", "Berlin"))
    print(h2("Hamburg", "Berlin"))
    print(h3("Hamburg", "Berlin"))
    print(h4("Hamburg", "Berlin"))