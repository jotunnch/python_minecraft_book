from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 14
y = 0
z = -8
block_type = 103
up = 1
mc.setBlock(x, y, z, block_type)

# stack em
block_type = block_type - 40
mc.setBlock(x, y + up, z, block_type)

# stack em
block_type = block_type - 100
mc.setBlock(x, y + up * 2, z, block_type)

# stack em
block_type = block_type + 40
mc.setBlock(x, y + up * 3, z, block_type)