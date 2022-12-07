import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        line = line.replace('-', ',')
        a,b,c,d = [int(x) for x in line.split(',')]
        if a < c and b < c:
            continue
        elif a > d and b > d:
            continue
        count += 1
    print(count)