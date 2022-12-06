import math

def calc_prio(ci):
    prio = 0
    aval = ord(ci)
    if 96 < aval < 123:
        prio = aval - 96
    elif 64 < aval < 91:
        prio = aval - 64 + 26
    else:
        print("mysko")
    return prio


def find_prio(ryggsack):
    split = math.floor(len(ryggsack) / 2)
    left = set(ryggsack[0:split])
    right = set(ryggsack[split:])

    ci = ''.join(left.intersection(right))
    return calc_prio(ci)


def main():
    inp = open("inputl3.txt")
    summa = 0

    for rucksack in inp:
        summa += find_prio(rucksack)

    inp.close()
    return summa

print(main())