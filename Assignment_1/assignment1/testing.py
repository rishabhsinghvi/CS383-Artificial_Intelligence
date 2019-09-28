from gridworld import Gridworld

grid = Gridworld("../gw/3.txt")

for i in range(0, 4):
    for j in range(0, 3):
        print(str(i) + "," + str(j))
        print(grid.successors((i,j)))
