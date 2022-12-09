#part 1
head = [0,0]
tail = [0,0]
tailpositions = []

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day09/input.txt","r") as input:
    line = input.readline()
    while line:
        split = line.split()
        for i in range(int(split[1])):
            #update head
            if split[0] == 'R':
                head[0] += 1
            elif split[0] == 'L':
                head[0] -= 1
            elif split[0] == 'U':
                head[1] += 1
            elif split[0] == 'D':
                head[1] -= 1
            
            #update tail
            if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1])>1:
                #same row or col
                if head[0] == tail[0] or head[1] == tail[1]:
                    if head[0] - tail[0] == 2:
                        tail[0] += 1
                    elif head[0] - tail[0] == -2:
                        tail[0] -= 1
                    elif head[1] - tail[1] == 2:
                        tail[1] += 1
                    elif head[1] - tail[1] == -2: 
                        tail[1] -= 1
                #diagnal
                else:
                    if head[0] > tail[0] and head[1] > tail[1]:
                        tail[0] += 1
                        tail[1] += 1
                    elif head[0] > tail[0] and head[1] < tail[1]:
                        tail[0] += 1
                        tail[1] -= 1
                    elif head[0] < tail[0] and head[1] < tail[1]:
                        tail[0] -= 1
                        tail[1] -= 1
                    elif head[0] < tail[0] and head[1] > tail[1]:
                        tail[0] -= 1
                        tail[1] += 1


            tailpositions.append(tuple(tail.copy()))
        line = input.readline()

print(len(set(tailpositions)))

#part 2
def update_tail(head, tail):
    if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1])>1:
        #same row or col
        if head[0] == tail[0] or head[1] == tail[1]:
            if head[0] - tail[0] == 2:
                tail[0] += 1
            elif head[0] - tail[0] == -2:
                tail[0] -= 1
            elif head[1] - tail[1] == 2:
                tail[1] += 1
            elif head[1] - tail[1] == -2: 
                tail[1] -= 1
            #diagnal
        else:
            if head[0] > tail[0] and head[1] > tail[1]:
                tail[0] += 1
                tail[1] += 1
            elif head[0] > tail[0] and head[1] < tail[1]:
                tail[0] += 1
                tail[1] -= 1
            elif head[0] < tail[0] and head[1] < tail[1]:
                tail[0] -= 1
                tail[1] -= 1
            elif head[0] < tail[0] and head[1] > tail[1]:
                tail[0] -= 1
                tail[1] += 1  
    return tail

rope = [[0,0] for i in range(10)]
head = rope[0]
tailpositions = []

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day09/input.txt","r") as input:
    line = input.readline()
    while line:
        split = line.split()
        for i in range(int(split[1])):
            #update head
            if split[0] == 'R':
                head[0] += 1
            elif split[0] == 'L':
                head[0] -= 1
            elif split[0] == 'U':
                head[1] += 1
            elif split[0] == 'D':
                head[1] -= 1
            
            for j in range(len(rope)-1):
                rope[j+1] = update_tail(rope[j],rope[j+1])
            
            tailpositions.append(tuple(rope[-1].copy()))
        line = input.readline()

print(len(set(tailpositions)))
                