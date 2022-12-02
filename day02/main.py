total = 0

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day02/input.txt","r") as input:
    line = input.readline()
    while line:
        if line[2] == 'X':
            if line[0] == 'A':
                total += 1 + 3
            elif line[0] == 'B':
                total += 1 + 0
            else:
                total += 1 + 6
        elif line[2] == 'Y':
            if line[0] == 'A':
                total += 2 + 6
            elif line[0] == 'B':
                total += 2 + 3
            else:
                total += 2 + 0
        else:
            if line[0] == 'A':
                total += 3 + 0
            elif line[0] == 'B':
                total += 3 + 6
            else:
                total += 3 + 3

        line = input.readline()
    
    print(total)