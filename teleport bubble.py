from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create("192.168.1.6") # add server ip
#base location and size varible
baseX= 100
baseY= 100
baseZ= 100
baseSize = 10
me = int(mc.conn.sendReceive(b"world.getPlayerId", "me"))

while True:
  players = mc.getPlayerEntityIds()#get all players
  
  for i in players:
    bP = mc.entity.getPos(i) # bad player
    
    if i != me:
      if (bP.x > baseX - baseSize and bP.x < baseX + baseSize and
      bP.y > baseY - baseSize and bP.y < baseY + baseSize and
      bP.z > baseZ - baseSize and bP.z< baseZ + baseSize):
        mc.postToChat("go away")
        mc.entity.setPos(i,255,255,255)   
  time.sleep(1)
