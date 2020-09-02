import numpy as np

#range
xrange = 10
yrange = 10

#for life calculation
area = np.zeros((3,3))

#stage
world = np.zeros((xrange,yrange))
worldTmp = np.zeros((xrange,yrange))

#game period
period = 500


#init
for i in range(yrange):
    for g in range(xrange):
        if np.random.rand() >= 0.2 :
            world[i,g] = 0
        else:
            world[i,g] = 1

print("***********************")
print(0)
print("***********************")
print(world)


#repeat until period
for gamecount in range(period):
    print("***********************")
    print(gamecount + 1)
    print("***********************")
    for i in range(yrange):
        for g in range(xrange):
            worldTmp[i,g] = world[i,g]
            area[0,0] = 0
            area[0,1] = 0
            area[0,2] = 0
            area[1,0] = 0
            area[1,1] = 0
            area[1,2] = 0
            area[2,0] = 0
            area[2,1] = 0
            area[2,2] = 0

            if (i - 1) >= 0 and (g - 1) >= 0:
                area[0,0] = world[i-1,g-1]

            if (i - 1) >= 0:
                area[0,1] = world[i-1,g]

            if (i - 1) >= 0 and (g + 1) < xrange:
                area[0,2] = world[i-1,g+1]

            if (g - 1) >= 0:
                area[1,0] = world[i,g-1]

            if (g + 1) < xrange:
                area[1,2] = world[i,g+1]

            if (i + 1) < yrange and (g - 1) >= 0:
                area[2,0] = world[i+1,g-1]

            if (i + 1) < yrange:
                area[2,1] = world[i+1,g]

            if (i + 1) < yrange and (g + 1) < xrange:
                area[2,2] = world[i+1,g+1]

            if (world[i,g] == 0 ) and (area[0,0] + area[0,1] + area[0,2] + area[1,0] + area[1,2] + area[2,0] + area[2,1] + area[2,2] == 3):
                worldTmp[i,g] = 1

            if (world[i,g] == 1 ) and ((area[0,0] + area[0,1] + area[0,2] + area[1,0] + area[1,2] + area[2,0] + area[2,1] + area[2,2] == 3) or (area[0,0] + area[0,1] + area[0,2] + area[1,0] + area[1,2] + area[2,0] + area[2,1] + area[2,2] == 2 )):
                worldTmp[i,g] = 1

            if (world[i,g] == 1 ) and ((area[0,0] + area[0,1] + area[0,2] + area[1,0] + area[1,2] + area[2,0] + area[2,1] + area[2,2] )<= 1 ):
                worldTmp[i,g] = 0

            if (world[i,g] == 1 ) and ((area[0,0] + area[0,1] + area[0,2] + area[1,0] + area[1,2] + area[2,0] + area[2,1] + area[2,2]) >= 4 ):
                worldTmp[i,g] = 0

    world = worldTmp

    print(world)
