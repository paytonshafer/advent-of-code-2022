import os
import unittest

def parse_input(input):
    return input.strip().split("\n")

def chdir(cwd, path):
    if path == "/":
        return []
    elif path == "..":
        return cwd[0:-1]
    else:
        assert ".." not in path
        return cwd + path.split("/")

def add_file(root, cwd, name, size):
    directory = root
    for e in cwd:
        if e not in directory:
            directory[e] = {}
        directory = directory[e]
    directory[name] = size

def calc_size(directories, path, directory):
    size = 0
    for k, v in directory.items():
        if isinstance(v, dict):
            size += calc_size(directories, path + "/" + k, v)
        else:
            size += v
    directories[path if path else "/"] = size
    return size

def build_tree(entries):
    cwd = []
    root = {}
    for e in entries:
        elems = e.split(" ")
        if elems[0] == "$" and elems[1] == "cd":
            cwd = chdir(cwd, elems[2])
        elif elems[0] == "$" and elems[1] == "ls":
            pass
        elif elems[0] == "dir":
            pass
        else:
            add_file(root, cwd, elems[1], int(elems[0]))
    return root

#Part 1
def solve1(entries):
    root = build_tree(entries)
    directories = {}
    calc_size(directories, "", root)
    return sum([v for v in directories.values() if v <= 100000])


with open(f"/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day07/input.txt") as f:
    entries = parse_input(f.read())
print(solve1(entries))

#part 2
def solve2(entries):
    root = build_tree(entries)
    directories = {}
    calc_size(directories, "/", root)

    used = directories["/"]
    total = 70000000
    unused = total - used
    need_to_delete = 30000000 - unused
    assert need_to_delete > 0
    return min([v for v in directories.values() if v >= need_to_delete])

with open(f"/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day07/input.txt") as f:
    entries = parse_input(f.read())
print(solve2(entries))