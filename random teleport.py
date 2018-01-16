from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create() # add server ip



#randomly teleports all players


players = mc.getPlayerEntityIds()

for i in players:
    mc.entity.setPos(i,randint(0,200),randint(0,200),randint(0,200))
