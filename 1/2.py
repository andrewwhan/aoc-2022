import sys
from queue import PriorityQueue

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    elves = PriorityQueue()
    current = 0
    for line in f:
        if(len(line.strip()) == 0):
            print("queueing")
            elves.put((-current, current))
            current = 0
        else:
            current += int(line)
    print(elves.get()[1] + elves.get()[1] + elves.get()[1])
