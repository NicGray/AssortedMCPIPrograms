from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create("192.168.1.6")


entityId= int(mc.conn.sendReceive(b"world.getPlayerId", ))
p = mc.entity.getPos(entityId)
prev = [0,0,0] #new
while True:

  p = mc.entity.getPos(entityId)
  
  if prev != [int(p.x),int(p.y),int(p.z)]: #new
    mc.setBlocks(prev[0]+1,prev[1]-1,prev[2]-1,
            prev[0]-1, prev[1]-1, prev[2]+1, block.AIR.id)
  
  mc.setBlocks(p.x+1,p.y-1,p.Z-1,
               p.x-1, p.y-1, p.z+1, block.GLASS.id)
  prev = [int(p.x),int(p.y),int(p.z)]#new
  time.sleep(0.001)
