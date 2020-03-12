# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -55.2
y = 110.3
z = -73.4

# Set x, y, and z variables to represent coordinates
mc.player.setPos(x, y, z)