#part 1
def uniqueChars(str):
    char_set = [False] * 128 #set False for each ASCII char
    for i in range(0, len(str)):
        val = ord(str[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True

with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day06/input.txt","r") as input:
    line = input.readlines()
    for i in range(len(line[0])):
        str = line[0][i:i+4]
        if uniqueChars(str):
            print(i+4)
            break
            i += 1

#part 2
with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day06/input.txt","r") as input:
    line = input.readlines()
    for i in range(len(line[0])):
        str = line[0][i:i+14]
        if uniqueChars(str):
            print(i+14)
            break
    