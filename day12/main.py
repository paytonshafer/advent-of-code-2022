from collections import defaultdict

#read map
def read_edges():
    with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day12/input.txt","r") as input:
        lines = input.readlines()
        edges = []
        top, bottom, left, right = True, True, True, True

        for j, line in enumerate(lines):
            if j == 0:
                top = False
            elif j == len(lines)-1:
                bottom = False
            else:
                top, bottom = True, True
            
            for i, c in enumerate(line):
                if i == 0:
                    left = False
                elif i == len(line)-2:
                    right = False
                elif i == len(line)-1:
                    break
                else:
                    left, right = True, True

                if c == "S":
                    if lines[j-1][i] == "a":
                        edges.append([str(i) + str(j), str(j-1) + str(i)])
                    if lines[j+1][i] == "a":
                        edges.append([str(i) + str(j), str(j+1) + str(i)])
                    if lines[j][i+1] == "a":
                        edges.append([str(i) + str(j), str(j) + str(i+1)])
                
                if c == "E":
                    if lines[j-1][i] == "z":
                        edges.append([str(i) + str(j), str(j-1) + str(i)])
                    if lines[j+1][i] == "z":
                        edges.append([str(i) + str(j), str(j+1) + str(i)])
                    if lines[j][i+1] == "z":
                        edges.append([str(i) + str(j), str(j) + str(i+1)])
                    if lines[j][i-1] == "z":
                        edges.append([str(i) + str(j), str(j) + str(i-1)])

                if top and (ord(c) + 1 == ord(lines[j-1][i]) or ord(c) >= ord(lines[j-1][i])) and not(lines[j-1][i] == "S" or lines[j-1][i] == "E"):
                    edges.append([str(i) + str(j), str(j-1) + str(i)])
                
                if bottom and (ord(c) + 1 == ord(lines[j+1][i]) or ord(c) >= ord(lines[j+1][i])) and not(lines[j+1][i] == "S" or lines[j+1][i] == "E"):
                    edges.append([str(i) + str(j), str(j+1) + str(i)])

                if right and (ord(c) + 1 == ord(lines[j][i+1]) or ord(c) >= ord(lines[j][i+1])) and not(lines[j][i+1] == "S" or lines[j][i+1] == "E"):
                    edges.append([str(i) + str(j), str(j) + str(i+1)])

                if left and (ord(c) + 1 == ord(lines[j][i-1]) or ord(c) >= ord(lines[j][i-1])) and not(lines[j][i-1] == "S" or lines[j][i-1] == "E"):
                    edges.append([str(i) + str(j), str(j) + str(i-1)])
    return edges
                
edges = read_edges()

def make_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge[0], edge[1]
         
        graph[a].append(b)
        graph[b].append(a)

    return graph

graph = make_graph(edges)

for list in graph.values():
    l = [*set(list)]
    list = l

def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
     
    if start == goal:
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            
                if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return
            explored.append(node)

    print("So sorry, but a connecting path doesn't exist :(")
    return

BFS_SP(graph, "S", "E")
print(graph["01"])