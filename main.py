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

schem = ""
terrainType = ""
# Create the block state we are going to use
#block = BlockState("minecraft:light_blue_concrete")

#------Functions------

# Build the schematic
def genStruct(structureType):
    if structureType == "house":
        # Shortcut to create a schematic with a single region
        reg = Region(0, 0, 0, 21, 21, 21)
        schem = reg.as_schematic(name="Creation1", author="Anonymous", description="Made with Schematic Editor, Powered by Litemapy")
        data = sg.createHouse()
        item = 0
        for y, z, x in reg.allblockpos():
            #print(z,y,x)
            item = (y+1)*441 + (z)*21 + x
            if item < len(data):
                if data[item] != "minecraft:air":
                    reg.setblock(x, y, z, BlockState(data[item]))

    elif structureType == "terrain":
        # Shortcut to create a schematic with a single region
        reg = Region(0, 0, 0, 80, 20, 80)
        schem = reg.as_schematic(name="Creation1", author="Anonymous", description="Made with Schematic Editor, Powered by Litemapy")
        data = sg.createTerrain()
        item = 0
        for x, y, z in reg.allblockpos():
            #print(z,y,x)
            item = (y+1)*6400 + (z)*80 + x
            if item < len(data):
                if data[item] != "minecraft:air":
                    reg.setblock(x, y, z, BlockState(data[item]))

    schem.save("creation.litematic")


# preview the schematic
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


openingFrame = tk.Frame(root, bg="#c9c9c9")
openingFrame.grid(padx=180,pady=200)

img = tk.PhotoImage(file="Schemedit.png")
label = tk.Label(
    root,
    image=img
)
label.place(x=0, y=0)



def openSaveMenu():
    '''
    root2 = tk.Tk()
    root2.geometry("200x100")
    root2.title("Rendering House")

    renderFrame = tk.Frame(root2, bg="blue")
    renderFrame.grid(padx=50,pady=50)

    renderText = tk.Label(renderFrame, text="Creating House...")
    renderText.pack()
    '''

    name = asksaveasfile(initialfile = 'Creation.litematic', mode='wb',defaultextension=".litematic", filetypes=[("Litematica Schematics","*.litematic")])
    schematicFile = open("creation.litematic", "rb")
    text2save = bytearray(schematicFile.read())
    #print(schematicFile)
    name.write(text2save)
    name.close

    root.destroy()
    #root2.destroy()

def house():
    genStruct(structureType="house")
    openSaveMenu()

def plains():
    terrainType ="plains"
    genStruct(structureType="terrain")
    openSaveMenu()

def hills():
    terrainType ="hills"
    genStruct(structureType="terrain")
    openSaveMenu()

def desert():
    terrainType ="desert"
    genStruct(structureType="terrain")
    openSaveMenu()
    
def icespikes():
    terrainType ="icespikes"
    genStruct(structureType="terrain")
    openSaveMenu()

def amplifiedmesa():
    terrainType ="amplifiedmesa"
    genStruct(structureType="terrain")
    openSaveMenu()


#renderFrame.tkraise()
openingFrame.tkraise()

#startText = tk.Label(openingFrame, text="Schemedit v1.0.1")
#startText.pack()

house = tk.Button(openingFrame, text="Generate Modern House ", command=house)
house.grid(row=0,column=0)

emptyspace1 = tk.Label(openingFrame, text="", bg="#c9c9c9", pady=20)
emptyspace1.grid(row=1,column=0)

plains = tk.Button(openingFrame, text="Generate Plains", command=plains)
plains.grid(row=2,column=0)

hills = tk.Button(openingFrame, text="Generate Hills", command=hills)
hills.grid(row=3,column=0)

desert = tk.Button(openingFrame, text="Generate Desert", command=desert)
desert.grid(row=4,column=0)

icespikes = tk.Button(openingFrame, text="Generate Ice Spikes", command=icespikes)
icespikes.grid(row=5,column=0)

amplifiedmesa = tk.Button(openingFrame, text="Generate Amplified Mesa", command=amplifiedmesa)
amplifiedmesa.grid(row=6,column=0)


#genStruct()


# Save the schematic
#schem.save("creation.litematic")


#saveMenu()


#------Mainloop------
root.mainloop()