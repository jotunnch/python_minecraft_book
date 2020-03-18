from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
block_type = 10

# trap
y = y - 1
mc.setBlock(x, y, z, block_type) 