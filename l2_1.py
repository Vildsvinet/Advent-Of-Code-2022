ax = 1 + 3
ay = 2 + 6
az = 3 + 0
bx = 1 + 0
by = 2 + 3
bz = 3 + 6
cx = 1 + 6
cy = 2 + 0
cz = 3 + 3

totscore = 0

inp = open('inputl2.txt')
for i in inp:
    line = i.strip("\n\r")
    print(line)
    if line == "A X":
        totscore += ax
    elif line == "A Y":
        totscore += ay
    elif line == "A Z":
        totscore += az
    elif line == "B X":
        totscore += bx
    elif line == "B Y":
        totscore += by
    elif line == "B Z":
        totscore += bz
    elif line == "C X":
        totscore += cx
    elif line == "C Y":
        totscore += cy
    elif line == "C Z":
        totscore += cz
    else:
        continue

print(totscore)
inp.close()