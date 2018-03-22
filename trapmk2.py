from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create("192.168.1.6") # add server ip
import time
players = mc.getPlayerEntityIds()
counter = -500
x = 60
y= 60
cubesize = 5
airsize = cubesize -1
for i in players:
  mc.entity.setPos(i,x,y, counter)
  p = mc.entity.getPos(i)
  
  print(i)
  mc.setBlocks(p.x-cubesize,p.y-cubesize,p.z-cubesize,p.x+cubesize,p.y+cubesize,p.z+cubesize, block.OBSIDIAN.id)
  mc.setBlocks(p.x-airsize,p.y-airsize,p.z-airsize,p.x+airsize,p.y+airsize,p.z+airsize, block.AIR.id)
  time.sleep(1)
  mc.postToChat("lol")
  mc.entity.setPos(i,x,y,counter)

  counter =+ 20

mc.postToChat("you need to teleport out")
