import numpy as np

################################################################
#########################GET INPUT##############################
################################################################

inp = open("inputl5.txt")

#the input is divided into two parts; the crate state and the moves
cratestack = []             #list of stack-lists
moves = []                  #list of move config-lists

#read the input and put it into these lists
part1 = True
for line in inp:
    if line != '\n' and part1:
        arr = list(line)
        cratestack.append(arr)
        #print(arr)
    elif line == '\n':
        part1=False
    elif line != '\n':
        moves.append(list(line.strip().split(' ')))

################################################################
######################MANIPULATE ARRAYS#########################
################################################################

#manipulate the cratestack array to be horisontal
#(one list per stack instead of one list per height)
horistontal_stacks = np.transpose(np.array(cratestack))
#remove empty rows
cratestacks = []
for row in horistontal_stacks:
    if row[-1] != ' ':
        cratestacks.append(list(row))
#remove row with only linebreaks
cratestacks.pop()

#reverse and only keep the boxes
for i in range(len(cratestacks)):
    cratestacks[i] = [j for j in cratestacks[i] if j != ' ']
    cratestacks[i].reverse()


#only keep the integers
for i in range(len(moves)):
    moves[i] = [int(m) for m in moves[i] if m.isdigit()]

################################################################
#################PROCEED WITH ALGORITHM#########################
################################################################

for i in range(len(moves)):
    amount = moves[i][0]
    origin = moves[i][1]
    target = moves[i][2]

    cratestacks[target-1] += cratestacks[origin-1][-amount:]
    cratestacks[origin-1] = cratestacks[origin-1][:-amount]


#print the result
topcrates = ''
for stack in cratestacks:
    topcrates += str(stack.pop())

print(topcrates)