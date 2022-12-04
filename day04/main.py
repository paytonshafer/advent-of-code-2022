import re

# returns true of A entirely contained in B otherwise false 
def removeElements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))

#part 1
total = 0
with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day04/input.txt","r") as input:
    line = input.readline()
    while line:
        ints = re.split(r'-|,|\n', line)
        ints = ints[:-1]
        ints = [int(i) for i in ints]
        first = [*range(ints[0],ints[1]+1)]
        second = [*range(ints[2],ints[3]+1)]
        if removeElements(first, second) or removeElements(second,first):
            total += 1
        line = input.readline()

    print(total)

#part 2
total = 0
with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day04/input.txt","r") as input:
    line = input.readline()
    while line:
        ints = re.split(r'-|,|\n', line)
        ints = ints[:-1]
        ints = [int(i) for i in ints]
        first = [*range(ints[0],ints[1]+1)]
        second = [*range(ints[2],ints[3]+1)]
        for x in first:
            if second.__contains__(x):
                total += 1
                break
        line = input.readline()

    print(total)