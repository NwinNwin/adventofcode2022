f = open("day8/input.txt", "r")
f_content = [i.rstrip() for i in f.readlines()]

trees = []
total = 0

#part2
def findTrees(l):
    try:
        return l.index(False) + 1
    except:
        return len(l)
#part1
for i in range(len(f_content)):
    for j in range(len(f_content[i])):
        if i==0 or j ==0 or i == len(f_content)-1 or j == len(f_content[i])-1:
            total += 1
        else:
            left = []
            for x in range(len(f_content[i][:j])):
                left.append(f_content[i][j] > f_content[i][x])
            right= []
            for x in range(len(f_content[i][j+1:])):
                right.append(f_content[i][j] > f_content[i][x+j+1])
            up = []
            for x in range(len(f_content[:i])):
                up.append(f_content[i][j] > f_content[x][j])
            down = []
            for x in range(len(f_content[i+1:])):
                down.append(f_content[i][j] > f_content[x+i+1][j])
            
            if all(left) or all(right) or all(up) or all(down):
                    total+= 1

            #part2
            trees.append(findTrees(left[::-1]) * findTrees(right) * findTrees(up[::-1]) * findTrees(down))

            

#part2

print(max(trees))
