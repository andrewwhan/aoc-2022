import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    line = f.readline()
    for i in range(len(line) - 13):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            exit()
