from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create("192.168.1.3") # add server ip
import time
players = mc.getPlayerEntityIds()
counter = -500
x = 60
y= 60
for i in players:
  
  p = mc.entity.getPos(i)
  
  print(i)
  mc.setBlocks(p.x-2,p.y-2,p.z-2,p.x+2,p.y+2,p.z+2, block.AIR.id)
 
  time.sleep(1)
  mc.postToChat("lol")

  counter =+ 20

mc.postToChat("you need to teleport out")
