# Import
import numpy as np

# Main

def checkIfInRange(x,y,z,c1x,c1y,c1z,c2x,c2y,c2z):
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
    
    # Next checks Y
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

    # Next checks Z
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
    return inRange

def fill(x1,y1,z1,x2,y2,z2,material):
    for cell in range(len(cells)):
        cellx = cell % 21
        celly = (np.floor(cell / 21)) % 21
        cellz = np.floor(cell / 441)
        if checkIfInRange(cellx,celly,cellz,x1,y1,z1,x2,y2,z2) == True:
            cells[cell] = material

def createHouse():
    global cells
    cells = []
    for i in range(21**3):
        cells.append("air")
    fill(3,3,3,10,10,10,"minecraft:light_blue_concrete")
    fill(6,6,6,19,19,19,"minecraft:light_blue_concrete")

    print(cells)
    return cells
    
