#------Import------

from litemapy import Schematic, Region, BlockState
import random
import structuregeneration as sg

#------Setup------

# Shortcut to create a schematic with a single region
reg = Region(0, 0, 0, 21, 21, 21)
schem = reg.as_schematic(name="Creation1", author="Anonymous", description="Made with Schematic Editor, Powered by Litemapy")

# Create the block state we are going to use
block = BlockState("minecraft:light_blue_concrete")

#------Functions------

# Build the schematic
def genStruct():
    data = sg.createHouse()
    item = 0
    for z, y, x in reg.allblockpos():
        #print(z,y,x)
        item = (z+1)*441 + (y)*21 + x
        if item < len(data):
            if data[item] == "minecraft:light_blue_concrete":
                reg.setblock(z, y, x, block)


# Preview the schematic
def preview():

    # Load the schematic and get its first region
    schem = Schematic.load("creation.litematic")
    reg = list(schem.regions.values())[0]

    
    for x in reg.xrange():
        for z in reg.zrange():
            b = reg.getblock(x, 10, z)
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