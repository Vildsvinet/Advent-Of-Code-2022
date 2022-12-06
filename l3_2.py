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


def find_prio(elf1, elf2, elf3):
    e1 = set(elf1)
    e2 = set(elf2)
    e3 = set(elf3)

    badge = e1.intersection(e2, e3)
    ci = ''.join(badge)
    print(badge)
    return calc_prio(ci)


def main():
    inp = open("inputl3.txt")
    summa = 0

    while True:
        e1 = inp.readline().strip()
        e2 = inp.readline().strip()
        e3 = inp.readline().strip()

        if e1!='' and e2!='' and e3!='':
            summa += find_prio(e1, e2, e3)
        else: break

    inp.close()
    return summa

print(main())