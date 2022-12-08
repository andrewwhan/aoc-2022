import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    max = 0
    current = 0
    for line in f:
        if(len(line.strip()) == 0):
            if current > max:
                max = current
            current = 0
        else:
            current += int(line)
    print(max)
