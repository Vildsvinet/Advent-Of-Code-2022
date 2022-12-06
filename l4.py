
def manip_elf_pair(elf_pair):
    li = elf_pair.strip().split(',')

    #left interval
    li_left = li[0].split('-')
    li_left_low = int(li_left[0])
    li_left_high = int(li_left[1])
    left=set()
    for i in range(li_left_low, li_left_high+1):
        left.add(i)

    #right interval
    li_right = li[1].split('-')
    li_right_low = int(li_right[0])
    li_right_high = int(li_right[1])
    right=set()
    for j in range(li_right_low, li_right_high+1):
        right.add(j)

    #part1:
    return (left.issubset(right) or left.issuperset(right))
    #part2:
    #return (not left.isdisjoint(right))


def main():
    summa = 0
    inp = open("inputl4.txt")
    for line in inp:
        if manip_elf_pair(line):
            summa += 1

    return summa

print(main())