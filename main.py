#------Import------

from tracemalloc import start
from turtle import bgcolor
from litemapy import Schematic, Region, BlockState
import random
import structuregeneration as sg
import tkinter as tk
import time
from tkinter.filedialog import asksaveasfile


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

    
    for z in reg.zrange():
        for y in reg.yrange():
            for x in reg.xrange():
                b = reg.getblock(x, 20-y, z)
                if b.blockid == "minecraft:air":
                    print(" ", end="")
                else:
                    print("#", end='')
            print()


#------Main------
root = tk.Tk()
root.geometry("500x500")
root.title("Schemedit v1.0.1")


openingFrame = tk.Frame(root, bg="black")
openingFrame.grid(padx=200,pady=200)



def openPreview():
    root2 = tk.Tk()
    root2.geometry("200x100")
    root2.title("Rendering House")

    renderFrame = tk.Frame(root2, bg="blue")
    renderFrame.grid(padx=50,pady=50)

    renderText = tk.Label(renderFrame, text="Creating House...")
    renderText.pack()

    name = asksaveasfile(initialfile = 'Creation.litematic', mode='w',defaultextension=".litematic", filetypes=[("Litematica Schematics","*.litematic")])
    text2save = str(open("creation.litematic"))
    name.write(text2save)
    name.close

#renderFrame.tkraise()
openingFrame.tkraise()

startText = tk.Label(openingFrame, text="Schemedit v1.0.1")
startText.pack()

startButton = tk.Button(openingFrame, text="Generate House", command=openPreview)
startButton.pack()





genStruct()


# Save the schematic
schem.save("creation.litematic")


preview()


#------Mainloop------
root.mainloop()