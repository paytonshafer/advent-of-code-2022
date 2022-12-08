sum = 0

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day08/input.txt","r") as input:
    lines = input.readlines()

    for i in range(len(lines)):
        if i == 0:
            sum += len(lines[i])-1
        elif i == len(lines) - 1:
            sum += len(lines[i])
        else:
            for j in range(len(lines[i])-1):
                if j == 0 or j == len(lines[i])-2:
                    sum += 1
                else:
                    passed = 0
                    current = int(lines[i][j])
                    for k in range(1,len(lines[i])-1-j):
                        right = int(lines[i][j+k])
                        if current <= right:
                            passed += 1
                            break
                    for k in range(1,j+1):
                        left = int(lines[i][j-k])
                        if current <= left:
                            passed += 1
                            break
                    for k in range(1,i+1):
                        above = int(lines[i-k][j])
                        if current <= above:
                            passed += 1
                            break
                    for k in range(1, len(lines)-i):
                        below = int(lines[i+k][j])
                        if current <= below:
                            passed += 1
                            break
                    if not (passed == 4):
                        sum += 1
print(sum)