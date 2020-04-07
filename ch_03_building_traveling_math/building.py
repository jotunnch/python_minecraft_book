from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0
# make walls
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

# hollow it out
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, air)

# add a swimming pool
width = 7
height = -2
length = 11
water = 4  
mc.setBlocks(x, y, z, x + width, y + height, z + length, air)