# Schemedit for Minecraft

Schemedit is a useful tool in automatically generating different structures for Minecraft. The structures can be locally saved as a .litematic file, which can be opened in minecraft using the Litematica mod. Schemedit allows users to automatically generate complex schematics, like detailed houses, which are randomly generated and unique, but have a distinct style.

### Modes

Schemedit has (as of June 2022) TWO different editors, including a modern house generator and a landscape generator.

The modern house generator is an automatic engine that produces interesting modern house designs that are visually unique every time they are generated. The shape and style of the elements are governed by parameters within the code, which changes them randomly with each iteration. Some of the elements include open-faced boxes, closed boxes, grill-type faces, and hedge gardens.

The landscape generator is an automatic engine which produce unique and visually interesting landscapes with adjustable vertical scale, to provide the best natural-looking environments as easily as possible. The shape of the landscape is determined by a series of subsequent processes. It begins with random noise, then uses neighboring averages to "blur the bitmap image. Then the new blurred image is clamped (dark gray becomes black, light gray becomes white) before it is blurred yet again. The blur-clamp process runs 5 times after which the details of the environment are large enough to be hills and valleys as opposed to random noise.

### Exporting

Schmedit allows the user to export .litematic files, which can be read and imported into Minecraft using the Litematica mod. Modern House schematics will have dimensions of 21 x 21 x 21, whereas Landscape schematics will have dimensions of 100 x 100 x 30.

### Credit

The process of converting the generated data into .litematic files could not have been possible without the library litemapy.