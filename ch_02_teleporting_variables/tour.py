# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Set x, y, and z variables to represent coordinates
x = -64
y = 110
z = -68

# change the players position
mc.player.setTilePos(x, y, z)

time.sleep(4)

# Set x, y, and z variables to represent coordinates
x = -115
y = 110
z = 114

# change the players position
mc.player.setTilePos(x, y, z)

time.sleep(4)

# Set x, y, and z variables to represent coordinates
x = -115 + 180

# change the players position
mc.player.setTilePos(x, y, z)

time.sleep(4)

# Set x, y, and z variables to represent coordinates
z = z - 180

# change the players position
mc.player.setTilePos(x, y, z)

time.sleep(4)

# Set x, y, and z variables to represent coordinates
x = -115 + 25.5
y = 110
z = 114 - 25.5

# change the players position
mc.player.setPos(x, y, z)