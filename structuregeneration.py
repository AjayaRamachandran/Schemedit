# Import
import numpy as np
import random as rand

# Main

def checkIfInRange(x,z,y,c1x,c1z,c1y,c2x,c2z,c2y):
    inRange = True
    # First checks X
    if c1x <= c2x:
        if x >= c1x and x <= c2x:
            ""
        else:
            inRange = False
    else:
        if x >= c2x and x <= c1x:
            ""
        else:
            inRange = False
    
    # Next checks z
    if c1z <= c2z:
        if z >= c1z and z <= c2z:
            ""
        else:
            inRange = False
    else:
        if z >= c2z and z <= c1z:
            ""
        else:
            inRange = False

    # Next checks y
    if c1y <= c2y:
        if y >= c1y and y <= c2y:
            ""
        else:
            inRange = False
    else:
        if y >= c2y and y <= c1y:
            ""
        else:
            inRange = False
    return inRange

def fill(x1,z1,y1,x2,z2,y2,material):
    for cell in range(len(cells)):
        cellx = cell % 21
        cellz = (np.floor(cell / 21)) % 21
        celly = np.floor(cell / 441)
        if checkIfInRange(cellx,cellz,celly,x1,z1,y1,x2,z2,y2) == True:
            cells[cell] = material

def base():
    x1 = 3
    z1 = 6
    y1 = 1
    x2 = 18
    z2 = 15
    y2 = 10
    fill(x1,z1,y1,x2,z2,y2,"minecraft:stone")

def emptyBox():
    # initialiye coordinates
    x1 = rand.randint(3,10)
    z1 = rand.randint(3,10)
    y1 = rand.randint(1,10)
    x2 = rand.randint(12,19)
    z2 = rand.randint(12,19)
    y2 = rand.randint(11,20)

    fill(x1,z1,y1,x2,z2,y2,"minecraft:smooth_quarty_block")
    fill(x1+1,z1,y1+1,x2-1,z2,y2-1,"minecraft:air")

def coveredBox():
    # initialiye coordinates
    x1 = rand.randint(3,10)
    z1 = rand.randint(3,10)
    y1 = rand.randint(1,10)
    x2 = rand.randint(12,19)
    z2 = rand.randint(12,19)
    y2 = rand.randint(11,20)

    fill(x1,z1,y1,x2,z2,y2,"minecraft:oak_planks")
    fill(x1+1,z1+1,y1+1,x2-1,z2-1,y2-1,"minecraft:air")



def createHouse():
    global cells
    cells = []
    for i in range(21**3):
        cells.append("minecraft:air")
    #fill(3,3,3,10,10,10,"minecraft:light_blue_concrete")
    #fill(6,6,6,19,19,19,"minecraft:light_blue_concrete")

    base()
    emptyBox()
    coveredBox()

    #print(cells)
    return cells
    
