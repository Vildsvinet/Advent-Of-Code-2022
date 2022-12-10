

''' example input
3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0
'''

#####one tree at a time solution#####
def vis_left(row, col, grid):
    tree = grid[row][col]
    for l in range (0, col):
        if grid[row][l] >= tree:
            return False
    return True

def vis_right(row, col, grid):
    tree = grid[row][col]
    for l in range(col+1, len(grid)):
        if grid[row][l] >= tree:
            return False
    return True

def vis_top(row, col, grid):
    tree = grid[row][col]
    for l in range(0, row):
        if grid[l][col] >= tree:
            return False
    return True

def vis_bot(row, col, grid):
    tree = grid[row][col]
    for l in range(row+1, len(grid)):
        if grid[l][col] >= tree:
            return False
    return True


def main():
    inp = open("input8.txt")
    grid = []

    for line in inp:
        grid.append(list(map(int,[*line.strip()])))
    inp.close()

    size = len(grid)
    vis_counter = 2 * size + 2 * (size - 2)
    print(vis_counter)

    #for tree in grid
    for i in range(1,size-1):
        for j in range(1,size-1):
            if vis_left(i,j,grid) or vis_right(i,j,grid) or vis_top(i,j,grid) or vis_bot(i,j,grid):
                vis_counter+=1
    return vis_counter

print(main())
