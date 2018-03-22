from mcpi.minecraft import Minecraft
import random as r
import time
mc = Minecraft.create("192.168.1.6") # add server ip



#randomly teleports all players

while True:
    players = mc.getPlayerEntityIds()


    for i in players:
        mc.postToChat("jump around")
        mc.entity.setPos(i,r.randint(0,200),r.randint(0,200),r.randint(0,200))
    time.sleep(1)
    print("done")

