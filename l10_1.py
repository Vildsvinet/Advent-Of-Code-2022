inp = open("input10.txt")

xreg = 1
cycles = 0
relevant_signal_strengths = []
totsign = 0

while cycles < 222:
    line = inp.readline()
    instr = line.strip().split(' ')
    if instr[0] == 'noop':
        cycles += 1
        if cycles % 40 == 20:
            strength = xreg * cycles
            relevant_signal_strengths.append(strength)
            totsign += strength
            print(xreg, ", ", cycles)
    elif instr[0] == 'addx':
        # print("hello")
        cycles += 1
        if cycles % 40 == 20:
            strength = xreg * cycles
            relevant_signal_strengths.append(strength)
            totsign += strength
            print(xreg, ", ", cycles)
        cycles += 1
        if cycles % 40 == 20:
            strength = xreg * cycles
            relevant_signal_strengths.append(strength)
            totsign += strength
            print(xreg, ", ", cycles)
        xreg += int(instr[1])

    else:
        print("oklart instruktion \n")
    # print(instr)


print(relevant_signal_strengths)
print(totsign)



























inp.close()
