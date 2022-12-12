#part 1
sum = 0

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day03/input.txt","r") as input:
    line = input.readline()
    while line:
        half1 = line[0:int(len(line)/2)]
        half2 = line[int(len(line)/2):len(line)+1]

        for x in half1:
            if half2.__contains__(x):
                s = str(x)
                if (s.islower()):
                    sum += ord(s) - 96 
                else:
                     sum += ord(s) - 38
                break

        line = input.readline()

    print(sum)

#part 2
sum = 0 #reset sum to 0

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day03/input.txt","r") as input:
    line = input.readline()
    while line:
        line2 = input.readline()
        line3 = input.readline()

        for x in line:
            if line2.__contains__(x) and line3.__contains__(x):
                if (x.islower()):
                    sum += ord(x) - 96 
                else:
                     sum += ord(x) - 38
                break

        line = input.readline()

    print(sum)