from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create("192.168.1.24") # add server ip



#bumps players


while True:
    
    players = mc.getPlayerEntityIds()
    
    for i in players:
        print(i)
        p = mc.entity.getPos(i)
        mc.entity.setPos(i,p.x+2,p.y+2,p.z+1)
    mc.postToChat("bumped")
    time.sleep(10)
