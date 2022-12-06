import numpy as np

inp = open("inputl5.txt")

biglist = []

for line in inp:
    if line != '\n':
        arr = list(line)
        biglist.append(arr)
        print(arr)
    else:
        break

print(biglist)

bigger = np.transpose(np.array(biglist))
#
print(bigger, '\n ______________________________________')

newbig = []

for row in bigger:
    if row[-1] != ' ':
        newbig.append(list(row))

print(newbig)



# test = [[0, 1, 4], [2, 3, 5]]
# test2 = np.transpose(test)
#
#
# print(test2)
