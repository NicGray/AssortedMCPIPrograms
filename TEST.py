from mcpi.minecraft import Minecraft

mc = Minecraft.create() # insert server ip here
#eg. mc = Minecraft.create('192.168.1.3')


mc.postToChat("It works!")


