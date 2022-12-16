import timeit


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

def main():
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

# print(main2())


m2time = timeit.timeit('main()', number=1)
print("second func:", m2time)
