from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import random
mc = Minecraft.create("192.168.1.6")
entityId = int(mc.conn.sendReceive(b"world.getPlayerId", "FruitierGravy61"))

places = list() #define out arrays
oldPos = list()
while True:
  for i in range(16): #we use 16 because thats how many wool col
    p= mc.entity.getPos(entityId) #gets the playrt pos
    mc.setBlock(p.x,p.y-1,p.z, block.WOOL.id, i) #places bloc
    newPos =[int(p.x),int(p.y-1), int(p.z)] #list of posistio
    if oldPos != newPos: # check if we have moved
      places.append(newPos)# adds a new block to places we
      #have been      
    for j in places: # interates through previous places
      num = random.uniform(1,16) # get a randomon colour
      mc.setBlock(j[0],j[1],j[2], block.WOOL.id, num)
    oldPos = newPos #save the previous pos
    time.sleep(0.01)#pause

