

''' example input
3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0
'''
import time


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
    # print(vis_counter)

    #for tree in grid
    for i in range(1,size-1):
        for j in range(1,size-1):
            if vis_left(i,j,grid) or vis_right(i,j,grid) or vis_top(i,j,grid) or vis_bot(i,j,grid):
                vis_counter+=1
    return vis_counter

print(main())


####################################
#####one row at a time solution#####
def vis_left2(grid, visgrid):
    highest = -1
    for row in range(len(grid)):
        for j in range(0, len(grid)):
            tree = grid[row][j]
            if tree > highest:
                visgrid[row][j] = 1
                highest = tree
        highest=-1

def vis_right2(grid, visgrid):
    highest = -1
    for row in range(len(grid)):
        for j in range(0, len(grid)):
            tree = grid[row][-(j+1)]
            if tree > highest:
                visgrid[row][-(j+1)] = 1
                highest = tree
        highest=-1

def vis_row_top(col, grid, visgrid):
    highest = -1

    for i in range(0, len(grid)):
        tree = grid[i][col]
        if tree > highest:
            visgrid[i][col] = 1
            highest = tree

def vis_row_bot(col, grid, visgrid):
    highest = -1

    for i in range(0, len(grid)):
        tree = grid[-(i+1)][col]
        if tree > highest:
            visgrid[-(i+1)][col] = 1
            highest = tree

def calc_ones(grid):
    tot = 0
    for row in grid:
        tot += row.count(1)
    return tot

def main2():
    inp = open("input8.txt")
    grid = []

    for line in inp:
        grid.append(list(map(int,[*line.strip()])))
    inp.close()

    size = len(grid)
    visibility_grid = [[0 for x in range(size)] for y in range(size)]

    vis_left2(grid, visibility_grid)
    vis_right2(grid, visibility_grid)
    for col in range(size):
        vis_row_top(col, grid, visibility_grid)
        vis_row_bot(col, grid, visibility_grid)

    return calc_ones(visibility_grid)

print(main2())


start = time.time()
print(main())
print("first version exec time:", time.time()-start)

start = time.time()
print(main2())
print("second version exec time:", time.time()-start)


