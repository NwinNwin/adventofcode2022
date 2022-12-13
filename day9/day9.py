#part 1
f = open("day9/input.txt", "r")
f_content = f.readlines()

tail = [0,0]
head = [0,0]

tail_visited = []

def print_moves(head, tail):
    print(f'head {head}, tail {tail}')
    

def right(num):
    # print("right")
    for i in range(num):
        head[0] += 1
        if head[1] == tail[1]:
            if head[0] - tail[0] == 2:
                tail[0] += 1
                tail_visited.append(tail[:])
        else:
            if head[0] - tail[0] == 2:
                tail[0] += 1
                if head[1] < tail[1]:
                    tail[1] -= 1
                else:
                    tail[1] += 1
                tail_visited.append(tail[:])
    #     print_moves(head,tail)
    # print("----------------------")

def up(num):
    # print("up")
    for i in range(num):
        head[1] += 1
        if head[0] == tail[0]:
            if head[1] - tail[1] == 2:
                tail[1] += 1
                tail_visited.append(tail[:])
        else:
            if head[1] - tail[1] == 2:
                tail[1] += 1
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                tail_visited.append(tail[:])
    #     print_moves(head,tail)
    # print("----------------------")

def left(num):
    # print("left")
    for i in range(num):
        head[0] -= 1
        if head[1] == tail[1]:
            if tail[0] - head[0] == 2:
                tail[0] -= 1
                tail_visited.append(tail[:])
        else:
            if tail[0] - head[0] == 2:
                tail[0] -= 1
                if head[1] < tail[1]:
                    tail[1] -= 1
                else:
                    tail[1] += 1
                tail_visited.append(tail[:])
    #     print_moves(head,tail)
    # print("----------------------")

def down(num):
    # print("down")
    for i in range(num):
        head[1] -= 1
        if head[0] == tail[0]:
            if tail[1] - head[1] == 2:
                tail[1] -= 1
                tail_visited.append(tail[:])
        else:
            if tail[1] - head[1] == 2:
                tail[1] -= 1
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                tail_visited.append(tail[:])
    #     print_moves(head,tail)
    # print("----------------------")

for ele in f_content:
    ele = ele.rstrip()
    ele = ele.split()
    if ele[0] == "U":
        up(int(ele[1]))
    if ele[0] == "L":
        left(int(ele[1]))
    if ele[0] == "D":
        down(int(ele[1]))
    if ele[0] == "R":
        right(int(ele[1]))


all_tails = [[0,0]]
for i in tail_visited:
    if i not in all_tails:
        all_tails.append(i)
print(len(all_tails))