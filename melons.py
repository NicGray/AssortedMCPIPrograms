from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()# enter server ip



#spawn melons on players

while True:
    players = mc.getPlayerEntityIds()
    for i in Players:
        x = i.x + 2
        y = i.y
        z = i.z + 2
        mc.setBlock(x, y, z, block.MELON.id)
    pause(1)

