import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        set_1 = {*line[:len(line)//2]}
        set_2 = {*line[len(line)//2:]}
        priority = ord(list(set_1.intersection(set_2))[0]) - 64
        if priority < 27:
            priority += 26
        else:
            priority -= 32
        sum += priority
    print(sum)