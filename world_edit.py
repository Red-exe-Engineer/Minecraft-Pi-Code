from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getArea():
    x = True
    while x == True:
        for hitBlock in mc.events.pollBlockHits():
            x, y, z = hitBlock.pos
    return(x, y, z)

chat = ""
while chat != "yes" and chat != "no":
    chat = str(input("Enable Chat Messages? messages will still be printed to consel [yes/no] "))
    if chat != "yes" and chat != "no":
        print("ERR: incorrect input '{}'".format(chat))

while True:
    x1, y1, z1 = getArea()
    print("Pos 1 {}".format([x1, y1, z1]))
    if chat == "yes":
        mc.postToChat("Pos 1 {}".format([x1, y1, z1]))
    
    x2, y2, z2 = getArea()
    print("Pos 2 {}".format([x2, y2, z2]))
    if chat == "yes":
        mc.postToChat("Pos 2 {}".format([x2, y2, z2]))
    
    blockWithData, fill, x = mc.getBlockWithData(x2, y2, z2), [0, 0], True
    mc.setBlock(x2, y2, z2, 247, 2)
    
    while x == True:
        for hitBlock in mc.events.pollBlockHits():
            
            x, y, z = hitBlock.pos
            fill = mc.getBlockWithData(x, y, z)
            
            if [x, y, z] == [x2, y2, z2]:
                fill, x1, y1, z1 = blockWithData, x2, y2, z2
            
        if mc.getBlock(x2, y2, z2) == 0:
            fill, x = 0, 0
    
    mc.setBlocks(x1, y1, z1, x2, y2, z2, fill)