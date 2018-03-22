from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create("192.168.1.6") # add server ip
import time
i= int(mc.conn.sendReceive(b"world.getPlayerId", "marsh_mello99"))


counter = -500
x = 60
y= 60

mc.entity.setPos(i,x,y, counter)
p = mc.entity.getPos(i)

print(i)
mc.setBlocks(p.x-2,p.y-2,p.z-2,p.x+2,p.y+2,p.z+2, block.OBSIDIAN.id)
mc.setBlocks(p.x-1,p.y-1,p.z-1,p.x+1,p.y+1,p.z+1, block.AIR.id)
time.sleep(1)
mc.postToChat("lol")
mc.entity.setPos(i,x,y,counter)

counter =+ 20

mc.postToChat("you need to teleport out")
