class Node:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        self.data += node.data

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child


root_node = Node(0, "/")
current_node = root_node

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day07/input.txt","r") as input:
    line = input.readlines()
    for i, str in enumerate(line):
        
        pass