import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    score = 0
    for line in f:
        line = line.split()
        opp = ord(line[0]) - 64
        goal = ord(line[1]) - 87
        me = (opp + goal - 2) % 3
        if(me == 0):
            me = 3
        score += me
        if me == opp:
            score += 3
        if (opp + 1) % 3 == me % 3:
            score += 6
        print(opp, me, score)
    print(score)