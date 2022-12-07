from operator import truediv
import sys

class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def print_tree(self, depth) -> None:
        print(' '*depth + f'{self.name}: {self.get_total_size()}')
        for c in self.children:
            c.print_tree(depth+1)
    
    def get_child(self, child_name) -> 'Directory':
        for c in self.children:
            if c.name == child_name:
                return c
        return None

    def get_total_size(self) -> int:
        return self.size + sum([x.get_total_size() for x in self.children])
    
    def traverse(self, needed_size) -> int:
        candidates = [x.traverse(needed_size) for x in self.children]
        candidates.append(self.get_total_size())
        candidates = list(filter(lambda x: x >= needed_size, candidates))
        if len(candidates) > 0:
            return min(candidates)
        else:
            return disk_space
        

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    disk_space = 70000000
    needed_space = 30000000
    root_dir = Directory('/', None)
    current_dir = root_dir
    for line in f:
        line_split = line.split()
        if line_split[0] == '$':
            if line_split[1] == 'cd':
                if line_split[2] == '/':
                    current_dir = root_dir
                elif line_split[2] == '..':
                    current_dir = current_dir.parent
                else:
                    child = current_dir.get_child(line_split[2])
                    if child == None:
                        child = Directory(line_split[2], current_dir)
                        current_dir.children.append(child)
                    current_dir = child
        elif line_split[0].isdigit():
            current_dir.size += int(line_split[0])
    print(root_dir.traverse(needed_space - disk_space + root_dir.get_total_size()))