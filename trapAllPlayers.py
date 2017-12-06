from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create() # add server ip

players = mc.getPlayerEntityIds()
counter = -500
x = 200
y= 200
for i in players:
    
    #Right Wall
    mc.setBlocks(x, y - 1, counter + 1, x, y + 2, counter + 1, block.OBSIDIAN)
    mc.setBlocks(x + 1, y - 1, counter + 1, x + 1, y + 2, counter + 1, block.OBSIDIAN)
    mc.setBlocks(x - 1, y - 1, counter + 1, x - 1, y + 2, counter + 1, block.OBSIDIAN)
    #Left Wall
    mc.setBlocks(x, y - 1, counter - 1, x, y + 2, counter - 1, block.OBSIDIAN)
    mc.setBlocks(x + 1, y - 1, counter - 1, x + 1, y + 2, counter - 1, block.OBSIDIAN)
    mc.setBlocks(x - 1, y - 1, counter - 1, x - 1, y + 2, counter - 1, block.OBSIDIAN)
    #Back Wall
    mc.setBlocks(x - 1, y - 1, counter, x - 1, y + 2, counter, block.OBSIDIAN)
    #Top
    mc.setBlocks(x - 1, y + 2, counter, x + 1, y + 2, counter, block.OBSIDIAN)
    #Bottom
    mc.setBlocks(x - 1, y - 1, counter, x + 1, y - 1, counter, block.OBSIDIAN)
    #FRONT Wall
    mc.setBlocks(x + 1, y - 1, counter, x+1 , y + 1, counter, block.OBSIDIAN)
    # torch
    mc.setBlock(x,y,counter, block.TORCH)
    
    
    mc.player.setPos(i,x,y,counter)

    counter =+ 20

mc.postToChat("you need to teleport out")
