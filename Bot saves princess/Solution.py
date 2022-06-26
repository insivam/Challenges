from math import floor


def displayPathtoPrincess(n, grid):
    mario, peach, solution = [floor(n/2), floor(n/2)], [], []

    for c, i in enumerate(grid):
        if 'p' in i:
            peach.append(c)
            peach.append(i.index('p'))

    if mario[0] < peach[0]:
        solution.extend(['DOWN'] * (peach[0]-mario[0]))
    elif mario[0] > peach[0]:
        solution.extend(['UP'] * (mario[0]-peach[0]))

    if mario[1] < peach[1]:
        solution.extend(['RIGHT'] * (peach[1]-mario[1]))
    elif mario[1] > peach[1]:
        solution.extend(['LEFT'] * (mario[1]-peach[1]))

    for i in solution:
        print(i)


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
