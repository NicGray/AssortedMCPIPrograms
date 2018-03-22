from mcpi.minecraft import Minecraft

import mcpi.block as block
mc = Minecraft.create('192.168.1.7')

for y in range(64,66):
  for x in range(-55, -20):
      mc.setBlock(x, y, 330, block.FENCE.id)

  for z in range(330, 341):
      mc.setBlock(-20, y, z, block.FENCE.id)


  for x in range(-55, -20):
      mc.setBlock(x, y, 340, block.FENCE.id)

  for z in range(330, 341):
      if z == 335:
          # Fence gate facing east
          mc.setBlock(-55, y, z, block.FENCE_GATE.id, 5)
      else:
          mc.setBlock(-55, y, z, block.FENCE.id)
print("done")
