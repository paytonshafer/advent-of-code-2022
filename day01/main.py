#Part 1
sum = 0
maxSum = 0

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day01/input.txt","r") as input:
    line = input.readline()
    while line:
        if (line == "\n"):
            if sum > maxSum:
                maxSum = sum
            sum = 0
        else:
            sum = sum + int(line)

        line = input.readline()

print(maxSum)


#Part 2
sum = 0
count = 0
maxSums = [0,0,0]

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day01/input.txt","r") as input:
    line = input.readline()
    while line:
        if (line == "\n"):
            if count == 0 or count == 1 or count ==2:
                maxSums[count] = sum
            elif min(maxSums) < sum:
                maxSums[maxSums.index(min(maxSums))] = sum
            count += 1
            sum = 0
        else:
            sum = sum + int(line)

        line = input.readline()

result = 0
for i in range(3):
    result = result + maxSums[i]
print(result)