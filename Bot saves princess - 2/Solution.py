def nextMove(n, r, c, grid):
    mario = [r, c]
    peach = []

    for counter, row in enumerate(grid):
        if 'p' in row:
            peach.append(counter)
            peach.append(row.index('p'))

    if mario[1] < peach[1]:
        return "RIGHT"
    elif mario[1] > peach[1]:
        return "LEFT"

    if mario[0] < peach[0]:
        return "DOWN"
    elif mario[0] > peach[0]:
        return "UP"


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
