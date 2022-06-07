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

def fill(x1,z1,y1,x2,z2,y2,material,material2,texture):
    for cell in range(len(cells)):
        cellx = cell % 21
        cellz = (np.floor(cell / 21)) % 21
        celly = np.floor(cell / 441)
        if checkIfInRange(cellx,cellz,celly,x1,z1,y1,x2,z2,y2) == True:
            if texture:
                choice = rand.randint(0,1)
                if choice == 0:
                    cells[cell] = material
                else:
                    cells[cell] = material2
            else:
                cells[cell] = material

def base():
    x1 = 3
    z1 = 6
    y1 = 1
    x2 = 18
    z2 = 15
    y2 = 5
    fill(x1,z1,y1,x2,z2,y2,"minecraft:stone", "minecraft:andesite", texture=True)
    x1 = 1
    z1 = 1
    y1 = 1
    x2 = 21
    z2 = 21
    y2 = 1
    fill(x1,z1,y1,x2,z2,y2,"minecraft:grass_block", "minecraft:moss_block", texture=True)
    x1 = 4
    z1 = 8
    y1 = 1
    x2 = 17
    z2 = 13
    y2 = 15
    fill(x1,z1,y1,x2,z2,y2,"minecraft:gray_concrete", "", texture=False)

def emptyBox():
    # initialize coordinates
    x1 = rand.randint(7,11)
    z1 = rand.randint(3,6)
    y1 = rand.randint(3,9)
    x2 = x1 + rand.randint(7,9)
    z2 = rand.randint(15,18)
    y2 = y1 + rand.randint(7,10)

    fill(x1,z1,y1,x2,z2,y2,"minecraft:smooth_quartz", "", texture=False)
    fill(x1+1,z1,y1+1,x2-1,z2,y2-1,"minecraft:air", "", texture=False)
    fill(x1+1,z1+1,y1+1,x2-1,z1+1,y2-1,"minecraft:white_stained_glass", "", texture=False)
    fill(x1+1,z2-1,y1+1,x2-1,z2-1,y2-1,"minecraft:white_stained_glass", "", texture=False)

def coveredBox():
    # initialize coordinates
    x1 = rand.randint(3,6)
    z1 = rand.randint(3,6)
    y1 = rand.randint(1,6)
    x2 = x1 + rand.randint(7,9)
    z2 = rand.randint(15,18)
    y2 = y1 + rand.randint(5,8)

    fill(x1,z1,y1,x2,z2,y2,"minecraft:oak_planks", "", texture=False)
    fill(x1+1,z1+1,y1+1,x2-1,z2-1,y2-1,"minecraft:air", "", texture=False)

def hedge(x):
    headerStart = 3
    headerGoal = 18
    header = headerStart
    while header < headerGoal:
        y = 2
        z = header
        fill(x,z,y,x,z,y,"minecraft:spruce_log", "", texture=False)
        
        y = 3
        z = header
        fill(x,z,y,x,z,y,"minecraft:oak_leaves", "", texture=False)
        
        y = 4
        z = header
        fill(x,z,y,x,z,y,"minecraft:oak_leaves", "", texture=False)
        
        header += 2




def createHouse():
    global cells
    cells = []
    for i in range(21**3):
        cells.append("minecraft:air")
    #fill(3,3,3,10,10,10,"minecraft:light_blue_concrete")
    #fill(6,6,6,19,19,19,"minecraft:light_blue_concrete")

    base()
    coveredBox()
    emptyBox()
    hedge(20)
    hedge(1)
    

    #print(cells)
    return cells
    
