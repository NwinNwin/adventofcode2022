f = open("dday11/input.txt", "r")
f_content = f.readlines()

import math

#part 1
class Monkey():
    def __init__(self, items, oper, test, test_true, test_false):
        self.items = items # [int] (list of items)
        self.oper = oper # "+ 3" (use eval)
        self.test = test # int (divisible num)
        self.test_true = test_true #int (monkey number)
        self.test_false = test_false #int (monkey number)
        self.times = 0
    
    def round(self):
        for old in self.items:
            new = eval(f'{old}{self.oper}')
            new = math.floor(new/3)
            if new % self.test == 0:
               eval(f'Monkey{self.test_true}.add({new})')
            else:
                eval(f'Monkey{self.test_false}.add({new})')
            self.times += 1
        self.items = []

    def add(self, item):
        self.items.append(item)
    
Monkey0 = Monkey([65, 58, 93, 57, 66], "* 7", 19, 6, 4)
Monkey1 = Monkey([76, 97, 58, 72, 57, 92, 82], "+ 4", 3, 7, 5)
Monkey2 = Monkey([90, 89, 96], "* 5", 13, 5, 1)
Monkey3 = Monkey([72, 63, 72, 99], "* old", 17, 0, 4)
Monkey4 = Monkey([65], "+ 1", 2, 6, 2)
Monkey5 = Monkey([97, 71], "+ 8", 11, 7, 3)
Monkey6 = Monkey([83, 68, 88, 55, 87, 67], "+ 2", 5, 2, 1)
Monkey7 = Monkey([64, 81, 50, 96, 82, 53, 62, 92], "+ 5", 7, 3, 0)

monkeys_list = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]

for i in range(20):
    for j in monkeys_list:
        j.round()
    
    # for x in monkeys_list:
    #     print(x.items)
    # print("-----------")

list_of_times = []
for i in monkeys_list:
    list_of_times.append(i.times)

list_of_times.sort()
print(list_of_times[-1] * list_of_times[-2])



