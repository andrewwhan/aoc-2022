import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    row = len(lines)
    col = len(lines[0])-1
    max = 0
    for x in range(col):
        for y in range(row):
            # down
            down = 0
            for j in range(y+1, row):
                if int(lines[j][x]) >= int(lines[y][x]):
                    down = j-y
                    break
                if j == row-1:
                    down = j-y
            # up
            up = 0
            for j in reversed(range(0, y)):
                if int(lines[j][x]) >= int(lines[y][x]):
                    up = y-j
                    break
                if j == 0:
                    up = y-j
            # right
            right = 0
            for i in range(x+1, col):
                if int(lines[y][i]) >= int(lines[y][x]):
                    right = i-x
                    break
                if i == col-1:
                    right = i-x
            # left
            left = 0
            for i in reversed(range(0, x)):
                if int(lines[y][i]) >= int(lines[y][x]):
                    left = x-i
                    break
                if i == 0:
                    left = x-i
            score = up*down*left*right
            if score > max:
                max = score
    print(max)

