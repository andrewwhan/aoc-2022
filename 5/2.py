import sys
import collections

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    line = f.readline()
    print(len(line))
    num_stacks = len(line)//4
    stack_container = {i:'' for i in range(num_stacks)}
    while line.strip()[0] != "1":
        for i in range(num_stacks):
            if line[1+i*4] != ' ':
                stack_container[i] = line[1+i*4]+stack_container[i]
        line = f.readline()
    f.readline() # spacer
    line = f.readline() # first move
    while len(line) > 0:
        command = line.split()
        stack_container[int(command[5])-1] += stack_container[int(command[3])-1][-int(command[1]):]
        stack_container[int(command[3])-1] = stack_container[int(command[3])-1][:-int(command[1])]
        line = f.readline()
        print(stack_container)
    result = ''
    for i in range(num_stacks):
        result += stack_container[i][-1]
    print(result)
