import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    row = len(lines)
    col = len(lines[0])-1
    vis_map = [[0 for i in range(col)] for j in range(row)]
    # top
    for i in range(col):
        max = -1
        for j in range(row):
            if int(lines[j][i]) > max:
                vis_map[j][i] = 1
                max = int(lines[j][i])
    # bottom
    for i in range(col):
        max = -1
        for j in reversed(range(row)):
            if int(lines[j][i]) > max:
                vis_map[j][i] = 1
                max = int(lines[j][i])
    # left
    for j in range(row):
        max = -1
        for i in range(col):
            if int(lines[j][i]) > max:
                vis_map[j][i] = 1
                max = int(lines[j][i])
    # right
    for j in range(row):
        max = -1
        for i in reversed(range(col)):
            if int(lines[j][i]) > max:
                vis_map[j][i] = 1
                max = int(lines[j][i])
    [print(row) for row in vis_map]
    total = sum([i for row in vis_map for i in row])
    print(total)

