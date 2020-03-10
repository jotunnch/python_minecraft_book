# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -64
y = 110
z = -68

# Set x, y, and z variables to represent coordinates
mc.player.setTilePos(x, y, z)