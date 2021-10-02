from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y-1, z, block.STONE)