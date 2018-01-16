from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create() # add server ip



#bumps players


while True:
    
    players = mc.getPlayerEntityIds()

    for i in players:
        mc.entity.setPos(i,i.x+2,i.y+1,i.z+1)
    pause(5)
