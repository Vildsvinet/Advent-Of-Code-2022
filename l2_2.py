totscore = 0

inp = open('inputl2.txt')
rock = 'A'
paper = 'B'
scissors = 'C'
lose = 'X'
draw = 'Y'
win = 'Z'
# win_over_rock = paper
# win_over_paper = scissors
# win_over_scissors = rock


def val(char):
    if char == 'A':
        return 1
    elif char == 'B':
        return 2
    elif char == 'C':
        return 3
    elif char == 'X':
        return 0
    elif char == 'Y':
        return 3
    elif char == 'Z':
        return 6
    else:
        print("something went wrong")


for line in inp:
    row = line.strip("\n\r").split(' ')
    totscore += val(row[1])

    if row[0] == rock:
        if row[1] == lose:
            totscore += val(scissors) #+ val(lose)
        elif row[1] == draw:
            totscore += val(rock) #+ val(draw)
        elif row[1] == win:
            totscore += val(paper) #+ val(win)
    elif row[0] == paper:
        if row[1] == lose:
            totscore += val(rock)
        elif row[1] == draw:
            totscore += val(paper)
        elif row[1] == win:
            totscore += val(scissors)
    elif row[0] == scissors:
        if row[1] == lose:
            totscore += val(paper)
        elif row[1] == draw:
            totscore += val(scissors)
        elif row[1] == win:
            totscore += val(rock)
    else:
        print("something went wrong")


print(totscore)


inp.close()
