from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# move me 5 spots
y = y + 10
mc.player.setTilePos(x, y, z)