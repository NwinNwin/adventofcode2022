f = open("day10/input.txt", "r")
f_content = f.readlines()

#part 1
# cycle = []
# x = 1

# for i in f_content:
#     i = i.rstrip()
#     if i.startswith("noop"):
#         cycle.append(x)
#     elif i.startswith("addx"):
#         cycle.append(x)
#         cycle.append(x)

#         num_add = int(i.split()[1])
#         x += num_add

# find_all = [19, 59, 99, 139,179,219]
# total = 0
# for i in find_all:
#     total += (i+1) * cycle[i]

# print(total)

#part 2
cycle = []
x = 1


def add_crt():
    if (len(cycle)+1) % 40 == 0:
            print('\n', end='')
    elif len(cycle)% 40 == x or len(cycle)% 40 == x-1 or len(cycle)% 40 == x+1:
        print('#', end='')
    else:
        print('.', end='')
        
    

for i in f_content:
    i = i.rstrip()

    if i.startswith("noop"):
        
        add_crt()
        cycle.append(x)
        
    elif i.startswith("addx"):
        add_crt()
        cycle.append(x)

        add_crt()
        cycle.append(x)


        num_add = int(i.split()[1])
        x += num_add
