from math import prod
#Monkey class to store each monkey
class Monkey:
    
    def __init__(self, items, operation, op_val, test_val, tmonk, fmonk):
        self.items = items
        self.operation = operation
        self.op_val = op_val
        self.test_val = test_val
        self.tmonk = tmonk
        self.fmonk = fmonk

    #function to calculate new stress val
    def new(self, item_num):
        if self.operation == "+":
            self.items[item_num] = self.items[item_num] + self.op_val
        elif self.operation == "*":
            if self.op_val == -1:
                self.items[item_num] = self.items[item_num]**2
            else:
                self.items[item_num] = self.items[item_num] * self.op_val

    #function to test which monkey to throw to   
    def test(self, item_num, divide):
        #Comment out below for part 2
        if divide:
            self.items[item_num] = int(self.items[item_num]/3)


        if self.items[item_num]%self.test_val == 0:
            return self.tmonk
        else: 
            return self.fmonk

#reading each monkey in
def get_monkeys(monkeys):
    with open("/Users/paytonshafer/Documents/GitHub/advent-of-code-2022/day11/input.txt","r") as input:
        line = input.readline()
        while line:
            if line == "\n":
                monkeys.append(Monkey(items, operation, op_val, test_val, tmonk, fmonk))
            else:
                split = line.split()
                
                if split[0] == "Monkey":
                    items = []
                    operation = ""
                    op_val = 0
                    test_val = 0
                    tmonk = 0
                    fmonk = 0
                elif split[0] == "Starting":
                    nums = line.split(",")
                    for i in range(len(nums)):
                        if i == len(nums)-1:
                            items.append(int(nums[i][-3:]))
                        else:
                            items.append(int(nums[i][-2:]))
                elif split[0] == "Operation:":
                    if split[4] == "+":
                        operation = "+"
                    elif split[4] == "*":
                        operation = "*"

                    if split[5] == "old":
                        op_val = -1
                    else:
                        op_val = int(split[5])
                elif split[0] == "Test:":
                    test_val = int(split[3])
                elif split[1] == "true:":
                    tmonk = int(split[5])
                elif split[1] == "false:":
                    fmonk = int(split[5])
            line = input.readline()

inspect_items = [0 for i in range(8)]

#running 20 rounds (part 1)
monkeys = []
get_monkeys(monkeys)
inspect_items = [0 for i in range(8)]

for i in range(20):
    for j in range(8):
        current_monk = monkeys[j]

        for k in range(len(current_monk.items)):
            inspect_items[j] += 1

            current_monk.new(0)
            new_monk = current_monk.test(0, True)
            monkeys[new_monk].items.append(current_monk.items.pop(0))

#answer for part 1
inspect_items.sort(reverse=True)
print(inspect_items[0]*inspect_items[1])

#running for 10000 rounds (part 2)
monkeys = []
get_monkeys(monkeys)
inspect_items = [0 for i in range(8)]
z = prod(m.test_val for m in monkeys)

for i in range(10000):
    for j in range(8):
        current_monk = monkeys[j]

        for k in range(len(current_monk.items)):
            inspect_items[j] += 1

            current_monk.new(0)
            new_monk = current_monk.test(0, False)
            monkeys[new_monk].items.append(current_monk.items.pop(0) % z)

#answer for part 2 
inspect_items.sort(reverse=True)
print(inspect_items[0]*inspect_items[1])