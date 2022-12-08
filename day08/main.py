#part 1
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

#part 2
current = 0
max = 0
score = 1

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day08/input.txt","r") as input:
    lines = input.readlines()
    for i in range(len(lines)):
        if i == 0 or i == len(lines) - 1:
            pass
        else:
            for j in range(len(lines[i])-1):
                if j == 0 or j == len(lines[i])-2:
                    pass
                else:
                    current = int(lines[i][j])
                    count = 0

                    for k in range(1,len(lines[i])-1-j):
                        right = int(lines[i][j+k])
                        count += 1

                        if current <= right:
                            score *= count
                            count = 0
                            break
                        elif k == len(lines[i])-2-j:
                            score *= count
                            count = 0

                    for k in range(1,j+1):
                        left = int(lines[i][j-k])
                        count += 1

                        if current <= left:
                            score *= count
                            count = 0
                            break
                        elif k == j:
                            score *= count
                            count = 0

                    for k in range(1,i+1):
                        above = int(lines[i-k][j])
                        count += 1

                        if current <= above:
                            score *= count
                            count = 0
                            break
                        elif k == i:
                            score *= count
                            count = 0

                    for k in range(1, len(lines)-i):
                        below = int(lines[i+k][j])
                        count += 1

                        if current <= below:
                            score *= count
                            count = 0
                            break
                        elif k == len(lines)-i-1:
                            score *= count
                            count = 0

                    if score > max:
                        max = score
                        
                    score = 1
print(max)