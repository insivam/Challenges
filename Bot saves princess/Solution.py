from math import floor


def displayPathtoPrincess(n, grid):
    mario = [floor(n/2), floor(n/2)]
    peach = []

    for c, i in enumerate(grid):
        if 'p' in i:
            peach.append(c)
            peach.append(i.index('p'))

    if mario[1] < peach[1]:
        print("RIGHT" * (peach[1]-mario[1]))
    elif mario[1] > peach[1]:
        print("LEFT" * (mario[1]-peach[1]))

    if mario[0] < peach[0]:
        print("DOWN"*(peach[0]-mario[0]))
    else:
        print("UP"*(mario[0]-peach[0]))


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
