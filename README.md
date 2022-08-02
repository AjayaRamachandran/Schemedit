<img src=https://i.ibb.co/xSQP99B/Minecraft-world1.jpg width="1000" height="125">
# Schemedit for Minecraft

Schemedit is a useful tool in automatically generating different structures for Minecraft. The structures can be locally saved as a .litematic file, which can be opened in minecraft using the Litematica mod. Schemedit allows users to automatically generate complex schematics, like detailed houses (which are randomly generated and unique, but have a distinct style) or natural terrain, with the ability to customize biome types for absolute control.

### Modes

Schemedit has (as of August 2022) TWO different main editors, including a modern house generator and a versatile landscape generator.

The modern house generator is an automatic engine that produces interesting modern house designs that are visually unique every time they are generated. The shape and style of the elements are governed by parameters within the code, which changes them randomly with each iteration. Some of the elements include open-faced boxes, closed boxes, grill-type faces, and hedge gardens.

The landscape generator is an automatic engine which produces unique and visually interesting landscapes with the ability to choose which biome it will generate. The biome specification changes many different things, from the block types all the way to the smoothness and vertical amplitude of the landscape's peaks and valleys. This allows the user to generate natural-looking environments but with the customization that regular minecraft doesn't really allow. The shape of the landscape is determined by a series of subsequent processes. It begins with random noise, then uses neighboring averages to "blur" the bitmap. Then the new blurred image is amplfied a bit (to avoid flatness) before it is blurred yet again. The blurring process runs a certain amount of times depending on which type of environment is selected.

Types of landscapes include: Plains, Desert, Mountains, Ice Spikes, and Amplified Mesa.

### Exporting

Schmedit allows the user to export .litematic files, which can be read and imported into Minecraft using the Litematica mod. Modern House schematics will have dimensions of 21 x 21 x 21, whereas Landscape schematics will have dimensions of 80 x 20 x 80.

### Credit

The process of converting the generated data into .litematic files could not have been possible without the library litemapy.
