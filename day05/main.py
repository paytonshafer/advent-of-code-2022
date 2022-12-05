with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day05/input.txt","r") as input:
    line = input.readline()

stacks = [[] for i in range(int(len(line)/4))]
print(len(stacks))


with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day05/input.txt","r") as input:
    line = input.readline()
    while line:
        for i in range(len(line)-1):
            if line[i] == '[':
                stacks[int(i/4)].insert(0, line[i+1])

        if line.startswith("move"):
            split = line.split()
            for i in range(int(split[1])):
                if not (len(stacks[int(split[3])-1]) == 0):
                    temp = stacks[int(split[3])-1].pop()
                    stacks[int(split[5])-1].append(temp)
        line = input.readline()

result = ""
for i in range(len(stacks)):
    result += stacks[i].pop()

print(result)
