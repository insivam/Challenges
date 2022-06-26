def displayPathtoPrincess(n, grid):
    mario = []
    peach = []

    for c, i in enumerate(grid):
        if 'p' in i:
            peach.append(c)
            peach.append(i.index('p'))
        if 'm' in i:
            mario.append(c)
            mario.append(i.index('m'))

    if mario[1] < peach[1]:
        for i in range(peach[1]-mario[1]):
            print("RIGHT")
    elif mario[1] > peach[1]:
        for i in range(mario[1]-peach[1]):
            print("LEFT")

    if mario[0] < peach[0]:
        for i in range(peach[0]-mario[0]):
            print("DOWN")
    elif mario[0] > peach[0]:
        for i in range(mario[0]-peach[0]):
            print("UP")


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
