from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
from random import randint
mc = Minecraft.create('192.168.2.3')  
#entityId = int(mc.conn.sendReceive(b"world.getPlayerId",
 #                                  "Festus32"))

#mc.entity.setPos(entityId, 120,100,160)
mc.postToChat("server about to restart")
players =mc.getPlayerEntityIds()
for i in range(60):
    time.sleep(0.5)
    mc.postToChat(str(60-i))
mc.postToChat("byebye")
##while 1==1 :
##    for i in players:
##        
##       # mc.entity.setPos(i,randint(100,1000),66, randint(100,1000))
##        p = mc.entity.getPos(i)
##        x= p.x
##        y= p.y
##        z= p.z
##        mc.setBlock(x, y+1, z+1, block.CACTUS.id)
##        
####        mc.setBlock(x, y+2, z, block.OBSIDIAN.id)
####        mc.setBlock(x-1, y, z, block.OBSIDIAN.id)
####        mc.setBlock(x+1, y, z, block.OBSIDIAN.id)
####        mc.setBlock(x, y, z+1, block.OBSIDIAN.id)
####        mc.setBlock(x, y, z-1, block.OBSIDIAN.id)
##    time.sleep(2)
