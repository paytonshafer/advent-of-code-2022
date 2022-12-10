#part 1
cycle = [1]
x = 1

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day10/input.txt","r") as input:
    line = input.readline()
    while line:
        split = line.split();
        if split[0] == "noop":
            cycle.append(x)
        if split[0] == "addx":
            cycle.append(x)
            x += int(split[1])
            cycle.append(x)

        line = input.readline()
    

print(20*cycle[19] + 60*cycle[59] + 100*cycle[99] + 140*cycle[139] + 180*cycle[179] + 220*cycle[219])\

#part 2
cycle = 0
x = 1
ans = ""
grid = ['.' for i in range(41)]
for i in range(3):
    grid[i] = "#"

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day10/input.txt","r") as input:
    line = input.readline()
    while line:
        split = line.split();
        if split[0] == "noop":
            ans += grid[cycle % 40]
            cycle += 1
        if split[0] == "addx":
            ans += grid[cycle % 40]
            cycle += 1
            ans += grid[cycle % 40]
            cycle += 1
            
            x += int(split[1])
            grid = ['.' for i in range(41)]
            for i in range(3):
                grid[(x-1)+i] = '#'

        line = input.readline()

answer = ''
for i in range(6):
    answer += ans[i*40:i*40+40]
    answer +='\n'
print(answer)