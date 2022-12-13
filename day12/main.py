from networkx import grid_2d_graph
from networkx import shortest_path

#read grid
with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day12/input.txt") as input:
    grid = [list(x.strip()) for x in input]

#make graph
source = None
sources = []
goal = None
for row_n, row in enumerate(grid):
    for col_n, c in enumerate(row):
        if c == "S":
            source = (row_n, col_n)
            grid[row_n][col_n] = "a"
        if c == "E":
            goal = (row_n, col_n)
            grid[row_n][col_n] = "z"
        if grid[row_n][col_n] == "a":
            sources.append((row_n, col_n))

g = grid_2d_graph(len(grid), len(grid[0]))

grid = [[ord(c)-ord("a") for c in row] for row in grid]
def weight_func(a, b, edge_dict):
    if grid[a[0]][a[1]] < grid[b[0]][b[1]] - 1:
        return None
    return 1

#part 1
print(len(shortest_path(g, source, goal, weight_func))-1)

#part2
paths = []
for s in sources:
    try:
        paths.append(len(shortest_path(g, s, goal, weight_func))-1)
    except:
        pass

print(min(paths))