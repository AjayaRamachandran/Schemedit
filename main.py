#------Import------

from litemapy import Schematic, Region, BlockState
import random
import turtle as trtl

#------Setup------

# Shortcut to create a schematic with a single region
reg = Region(0, 0, 0, 100, 100, 100)
schem = reg.as_schematic(name="Creation1", author="Anonymous", description="Made with Schematic Editor, Powered by Litemapy")

# Create the block state we are going to use
block = BlockState("minecraft:light_blue_concrete")


previewScreen = trtl.Screen()
previewScreen.setup(500,500)
previewScreen.title('Schematic Preview')

drawer = trtl.Turtle()
drawer.hideturtle()
drawer.goto(-100, 0)

#------Functions------

# Build the schematic
def genStruct():
    for x, y, z in reg.allblockpos():
        if random.randint(0,1) == 1:
            reg.setblock(x, y, z, block)


# Preview the schematic
def preview():

    # Load the schematic and get its first region
    schem = Schematic.load("creation.litematic")
    reg = list(schem.regions.values())[0]


    for x in reg.xrange():
        drawer.goto(drawer.xcor() += 1, drawer.ycor())
        for y in reg.zrange():
            drawer.goto()
            for z in reg.yrange():
                b = reg.getblock(x, y, z)
                if b.blockid == "minecraft:air":
                    drawer.pendown()
                    drawer.penup()

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

previewScreen.mainloop()