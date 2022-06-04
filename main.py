#------Import------

from litemapy import Schematic, Region, BlockState
import random
import structuregeneration as sg

#------Setup------

# Shortcut to create a schematic with a single region
reg = Region(0, 0, 0, 21, 21, 21)
schem = reg.as_schematic(name="Creation1", author="Anonymous", description="Made with Schematic Editor, Powered by Litemapy")

# Create the block state we are going to use
#block = BlockState("minecraft:light_blue_concrete")

#------Functions------

# Build the schematic
def genStruct():
    data = sg.createHouse()
    item = 0
    for y, z, x in reg.allblockpos():
        #print(z,y,x)
        item = (y+1)*441 + (z)*21 + x
        if item < len(data):
            if data[item] != "minecraft:air":
                reg.setblock(x, y, z, BlockState(data[item]))


# Preview the schematic
def preview():

    # Load the schematic and get its first region
    schem = Schematic.load("creation.litematic")
    reg = list(schem.regions.values())[0]

    
    for y in reg.yrange():
        for x in reg.xrange():
            b = reg.getblock(x, 20-y, 10)
            if b.blockid == "minecraft:air":
                print(" ", end="")
            else:
                print("#", end='')
        print()


#------Main------

genStruct()


# Save the schematic
schem.save("creation.litematic")


preview()