from mcpi.minecraft import Minecraft
import mcpi.block as block
import random as r
mc = Minecraft.create("192.168.1.5") # add server ip
import time


#randomly teleports all players



while True:
  players = mc.getPlayerEntityIds()
  print(players)
  for i in players:
    print(i)
    p = mc.entity.getPos(i)
    mc.setBlock(p.x,p.y+2,p.z, block.GRAVEL.id)
    mc.setBlock(p.x,p.y,p.z, block.COBWEB.id)
    time.sleep(1)
