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
            if texture: # If the texture boolean parameter is true, then fill command randomly chooses between two materials
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
    fill(x1,z1,y1,x2,z2,y2,"minecraft:stone", "minecraft:andesite", texture=True) # constructs the stone base
    x1 = 1
    z1 = 1
    y1 = 1
    x2 = 21
    z2 = 21
    y2 = 1
    fill(x1,z1,y1,x2,z2,y2,"minecraft:grass_block", "minecraft:moss_block", texture=True) # creates the flat grass ground
    x1 = 4
    z1 = 8
    y1 = 1
    x2 = 17
    z2 = 13
    y2 = 15
    fill(x1,z1,y1,x2,z2,y2,"minecraft:gray_concrete", "", texture=False) # creates the central concrete mass

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
    fill(x1+1,z2-1,y1+1,x2-1,z2-1,y2-1,"minecraft:white_stained_glass", "", texture=False) # generates a 4-sided hollow quartz cuboid with the two open sides stained glass

def coveredBox():
    # initialize coordinates
    x1 = rand.randint(3,6)
    z1 = rand.randint(3,6)
    y1 = rand.randint(1,6)
    x2 = x1 + rand.randint(7,9)
    z2 = rand.randint(15,18)
    y2 = y1 + rand.randint(5,8)

    fill(x1,z1,y1,x2,z2,y2,"minecraft:oak_planks", "", texture=False)
    fill(x1+1,z1+1,y1+1,x2-1,z2-1,y2-1,"minecraft:air", "", texture=False) # generates a hollow 6-sided wooden cuboid

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

        # creates the trimmed hedges lining the sides




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
    
def createTerrain(environmentType):
    global cells
    cells = []
    elevationData = []
    for i in range(128000): # formats list
        cells.append("minecraft:air")

    newElevationData = []
    for x in range(80): # randomly generates height values
        for z in range(80):
            elevationData.append(rand.randint(5,20))
            newElevationData.append(0)

    if environmentType == "hills":
        for num in range(15): # environment is pretty smooth
            for i in range(len(elevationData)):
                if i > 80 and i < 6320:
                    newElevationData[i] = (elevationData[i] + elevationData[i + 1] + elevationData[i - 1] + elevationData [i + 80] + elevationData [i - 80]) / 5
                else:
                    newElevationData[i] = (elevationData[i] + 12.5) / 2

            for i in range(len(elevationData)):
                elevationData[i] = newElevationData[i]

            for i in range(len(elevationData)):
                elevationData[i] = ((elevationData[i] - 12.5) * 1.15) + 12.5 # 1.15 means the vertical variation is relatively high
        
        for cell in range(len(cells)):
            cellx = cell % 80
            cellz = (np.floor(cell / 80)) % 80
            celly = np.floor(cell / 6400)

            if celly == np.round(elevationData[int(cellz * 80 + cellx)]): #if block is on the surface, make it grass
                cells[cell] = "minecraft:grass_block"
            elif celly <= elevationData[int(cellz * 80 + cellx)] and celly > elevationData[int(cellz * 80 + cellx)] - rand.randint(2,5): # if block is near surface, make it dirt
                cells[cell] = "minecraft:dirt"
            elif celly <= elevationData[int(cellz * 80 + cellx)]: # if block is below that, make it mostly stone but partly andesite
                blockChance = rand.randint(1,4)
                if blockChance == 1:
                    cells[cell] = "minecraft:andesite"
                else:
                    cells[cell] = "minecraft:stone"



    elif environmentType == "plains":
        for num in range(20): # environment is very smooth
            for i in range(len(elevationData)):
                if i > 80 and i < 6320:
                    newElevationData[i] = (elevationData[i] + elevationData[i + 1] + elevationData[i - 1] + elevationData [i + 80] + elevationData [i - 80]) / 5
                else:
                    newElevationData[i] = (elevationData[i] + 12.5) / 2

            for i in range(len(elevationData)):
                elevationData[i] = newElevationData[i]

            for i in range(len(elevationData)):
                elevationData[i] = ((elevationData[i] - 12.5) * 1.02) + 12.5 # 1.02 means that vertical veriation is very low
        
        for cell in range(len(cells)):
            cellx = cell % 80
            cellz = (np.floor(cell / 80)) % 80
            celly = np.floor(cell / 6400)

            if celly == np.round(elevationData[int(cellz * 80 + cellx)]): #if block is on the surface, make it grass
                cells[cell] = "minecraft:grass_block"
            elif celly <= elevationData[int(cellz * 80 + cellx)] and celly > elevationData[int(cellz * 80 + cellx)] - rand.randint(2,5): # if block is near surface, make it dirt
                cells[cell] = "minecraft:dirt"
            elif celly <= elevationData[int(cellz * 80 + cellx)]: # if block is below that, make it mostly stone but partly andesite
                blockChance = rand.randint(1,4)
                if blockChance == 1:
                    cells[cell] = "minecraft:andesite"
                else:
                    cells[cell] = "minecraft:stone"



    elif environmentType == "desert":
        for num in range(10): # environment is not smooth
            for i in range(len(elevationData)):
                if i > 80 and i < 6320:
                    newElevationData[i] = (elevationData[i] + elevationData[i + 1] + elevationData[i - 1] + elevationData [i + 80] + elevationData [i - 80]) / 5
                else:
                    newElevationData[i] = (elevationData[i] + 12.5) / 2

            for i in range(len(elevationData)):
                elevationData[i] = newElevationData[i]

            for i in range(len(elevationData)):
                elevationData[i] = ((elevationData[i] - 12.5) * 1.05) + 12.5 # 1.05 means that vertical variation is relatively low
        
        for cell in range(len(cells)):
            cellx = cell % 80
            cellz = (np.floor(cell / 80)) % 80
            celly = np.floor(cell / 6400)

            if celly == np.round(elevationData[int(cellz * 80 + cellx)]): #if block is on the surface, make it sand
                cells[cell] = "minecraft:sand"
            elif celly <= elevationData[int(cellz * 80 + cellx)] and celly > elevationData[int(cellz * 80 + cellx)] - rand.randint(2,5): # if block is near surface, make it sandstone
                cells[cell] = "minecraft:sandstone"
            elif celly <= elevationData[int(cellz * 80 + cellx)]: # if block is below that, make it mostly stone but partly andesite
                blockChance = rand.randint(1,4)
                if blockChance == 1:
                    cells[cell] = "minecraft:andesite"
                else:
                    cells[cell] = "minecraft:stone"


    
    elif environmentType == "icespikes":
        for num in range(10): # environment is not smooth
            for i in range(len(elevationData)):
                if i > 80 and i < 6320:
                    newElevationData[i] = (elevationData[i] + elevationData[i + 1] + elevationData[i - 1] + elevationData [i + 80] + elevationData [i - 80]) / 5
                else:
                    newElevationData[i] = (elevationData[i] + 12.5) / 2

            for i in range(len(elevationData)):
                elevationData[i] = newElevationData[i]

            for i in range(len(elevationData)):
                elevationData[i] = ((elevationData[i] - 12.5) * 1.3) + 12.3 # 1.3 means that vertical variation is very high
        
        for cell in range(len(cells)):
            cellx = cell % 80
            cellz = (np.floor(cell / 80)) % 80
            celly = np.floor(cell / 6400)

            if celly <= elevationData[int(cellz * 80 + cellx)]: # if block is below or at surface, make it packed ice
                cells[cell] = "minecraft:packed_ice"



    elif environmentType == "amplifiedmesa":
        for num in range(10): # environment is not smooth
            for i in range(len(elevationData)):
                if i > 80 and i < 6320:
                    newElevationData[i] = (elevationData[i] + elevationData[i + 1] + elevationData[i - 1] + elevationData [i + 80] + elevationData [i - 80]) / 5
                else:
                    newElevationData[i] = (elevationData[i] + 12.5) / 2

            for i in range(len(elevationData)):
                elevationData[i] = newElevationData[i]

            for i in range(len(elevationData)):
                elevationData[i] = ((elevationData[i] - 12.5) * 2) + 12.5 # 2 means that vertical variation is extremely high
        
        for cell in range(len(cells)):
            cellx = cell % 80
            cellz = (np.floor(cell / 80)) % 80
            celly = np.floor(cell / 6400)

            if celly <= elevationData[int(cellz * 80 + cellx)]: # if block is below or at surface, make it colored based on elevation
                if celly > 15:
                    cells[cell] = "minecraft:orange_terracotta"
                elif celly > 10:
                    cells[cell] = "minecraft:brown_terracotta"
                elif celly > 5:
                    cells[cell] = "minecraft:white_terracotta"
                else:
                    cells[cell] = "minecraft:yellow_terracotta"
    #print(cells[1202])
    

    #print(cells)
    return cells

