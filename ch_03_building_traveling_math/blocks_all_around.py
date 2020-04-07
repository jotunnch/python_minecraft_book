from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
block_type = 79

# make ice floor 3 spots away
x = x + 3
y = y - 1

# make a circle of ice
mc.setBlock(x, y, z, block_type)
mc.setBlock(x, y, z - 1, block_type)
mc.setBlock(x, y, z + 1, block_type)
mc.setBlock(x, y, z - 2, block_type)
mc.setBlock(x, y, z + 2, block_type)
mc.setBlock(x, y, z - 3, block_type)
mc.setBlock(x, y, z + 3, block_type)
mc.setBlock(x - 1, y, z - 3, block_type)
mc.setBlock(x - 1, y, z + 3, block_type)
mc.setBlock(x - 2, y, z - 3, block_type)
mc.setBlock(x - 2, y, z + 3, block_type)
mc.setBlock(x - 3, y, z - 3, block_type)
mc.setBlock(x - 3, y, z + 3, block_type)
mc.setBlock(x - 4, y, z - 3, block_type)
mc.setBlock(x - 4, y, z + 3, block_type)
mc.setBlock(x - 5, y, z - 3, block_type)
mc.setBlock(x - 5, y, z + 3, block_type)
mc.setBlock(x - 5, y, z - 2, block_type)
mc.setBlock(x - 5, y, z + 2, block_type)
mc.setBlock(x - 5, y, z - 1, block_type)
mc.setBlock(x - 5, y, z + 1, block_type)
mc.setBlock(x - 5, y, z, block_type)

