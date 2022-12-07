import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    sum = 0
    for i in range(len(lines)//3):
        set_1 = {*lines[i*3].strip()}
        set_2 = {*lines[i*3+1].strip()}
        set_3 = {*lines[i*3+2].strip()}
        priority = ord(list(set_1.intersection(set_2).intersection(set_3))[0]) - 64
        if priority < 27:
            priority += 26
        else:
            priority -= 32
        sum += priority
    print(sum)
