__author__ = 'jeshon.assuncao & rey.tom'
# -*-coding:Latin-1 -* 
from math import sqrt
from Town import Town

# 1) Le choix de l'heuristique influence le nombre de noeud visites, même si on
# obtiendra toujours un résultat optimal. Certaines heuristiques visiteront plus ou
# moin de noeuds avant d'arriver à la destination finale.
# 2) Les heuristiques h1 et h2 entre Vienne et Belgrade.
# 3) L'heuristiques numéro 3 semble la plus proche de la réalité et donne des résultats idéaux

connections = [] # Create our array of connections
positions = [] # Create our array of positions

def Astar(townA, townB, funcHeuristique):
    townVisited = Town(townA)
    townFinal = Town(townB)
    frontiere = []
    frontiere.append(townVisited)
    history = []

    while frontiere :
        town = frontiere.pop(0)
        history.append(town.name)

        if town.final(history, townB):
            return town.name

        #if townFinal.final(frontiere,townB):   Test si la ville finale est dans frontière
            #return townB.name

        ops = town.applicableOps(history, funcHeuristique, connections)

        print("[Town in visit] : ", town.name)
        print("[History] : ", history)
        print("[Childs] : ", ops)

        for op in ops :
            newTown = op
            newTownIsInFrontier = False

            for frontiereTownName in frontiere:
                if(newTown.name == frontiereTownName.name):
                    newTownIsInFrontier = True
                    break

            if newTownIsInFrontier == False and (newTown.name not in history) and newTown.legal(connections) :
                frontiere.append(newTown)

        frontiere.sort(key = lambda x:x.resultHeur)
        if (town.final(history, townB) == True):
            return town.name
        print("[Frontiere] : ",frontiere)
        print("\n")

    return "Pas de solution "

def h0(n,B):
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

    print("Using h0")
    print(Astar("Brussels", "Madrid", h0))
    print("Using h1")
    print(Astar("Brussels", "Madrid", h1))
    print("Using h2")
    #print(Astar("Brussels", "Madrid", h2))
    #print("Using h3")
    #print(Astar("Brussels", "Madrid", h3))
    #print("Using h4")
    #print(Astar("Brussels", "Madrid", h4))