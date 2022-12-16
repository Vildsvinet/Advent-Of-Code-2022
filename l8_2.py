''' example input
3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0
'''


def look_left(row, col, grid):      # samma rad
    this_height = grid[row][col]
    # print("current tree is ", this_height, " m high \n")
    vis_trees = 0
    for c in range(col):
        # print("looking at tree ", grid[row][col-c-1], " m high \n")
        if grid[row][col-c-1] < this_height:
            vis_trees +=1
        elif grid[row][col-c-1] >= this_height:
            vis_trees += 1
            break
        else: break
    return vis_trees

def look_right(row, col, grid):      # samma rad
    this_height = grid[row][col]
    # print("current tree is ", this_height, " m high \n")
    vis_trees = 0
    for c in range(len(grid) - col - 1):
        curr_tree = grid[row][col+c+1]
        # print("looking at tree ", curr_tree, " m high \n")
        if curr_tree < this_height:
            vis_trees +=1
        elif curr_tree >= this_height:
            vis_trees += 1
            break
        else: break
    return vis_trees

def look_up(row, col, grid):        # col constant
    this_height = grid[row][col]
    # print("current tree is ", this_height, " m high \n")
    vis_trees = 0
    for r in range(row):
        curr_tree = grid[row - r - 1][col]
        # print("looking at tree ", curr_tree, " m high \n")
        if curr_tree < this_height:
            vis_trees +=1
        elif curr_tree >= this_height:
            vis_trees += 1
            break
        else: break
    return vis_trees

def look_down(row, col, grid):        # col constant
    this_height = grid[row][col]
    # print("current tree is ", this_height, " m high \n")
    vis_trees = 0
    for r in range(len(grid) - row -1):
        curr_tree = grid[row + r + 1][col]
        # print("looking at tree ", curr_tree, " m high \n")
        if curr_tree < this_height:
            vis_trees +=1
        elif curr_tree >= this_height:
            vis_trees += 1
            break
        else: break
    return vis_trees
#
# print("vis_number ", look_down(0,2,grid))



def main():
    inp = open("input8.txt")
    grid = []
    scenic_highscore = 0
    scenic_score = 0

    for line in inp:
        grid.append(list(map(int,[*line.strip()])))
    inp.close()

    size = len(grid)

    #for tree in grid
    for i in range(0,size):
        for j in range(0,size):
            scenic_score = look_left(i, j, grid) * look_right(i, j, grid) * look_up(i, j, grid) * look_down(i, j, grid)
            if scenic_score > scenic_highscore:
                scenic_highscore = scenic_score

    return scenic_highscore



print("scenic highscore was ", main())




