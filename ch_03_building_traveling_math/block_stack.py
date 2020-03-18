from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 16
y = 0
z = -5
block_type = 103
mc.setBlock(x, y, z, block_type)

# stack em
y = y + 1
block_type = block_type - 40
mc.setBlock(x, y, z, block_type)

# stack em
y = y + 1
block_type = block_type - 100
mc.setBlock(x, y, z, block_type)

# stack em
block_type = block_type + 40
y = y + 1
mc.setBlock(x, y, z, block_type)