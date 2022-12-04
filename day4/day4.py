f = open("day4/input.txt", "r")
f_content = f.readlines()


#part1
total = 0
total2 = 0

for j in f_content:
    content = j.rstrip()
    content2 = content.split(",")
    ele1 = list(range(int(content2[0].split("-")[0]), int(content2[0].split("-")[1]) +1))
    ele2 = list(range(int(content2[1].split("-")[0]), int(content2[1].split("-")[1])+1))
    if all(i in ele1 for i in ele2) or all(e in ele2 for e in ele1):
        total +=1

#part2
for j in f_content:
    content = j.rstrip()
    content2 = content.split(",")
    ele1 = list(range(int(content2[0].split("-")[0]), int(content2[0].split("-")[1]) +1))
    ele2 = list(range(int(content2[1].split("-")[0]), int(content2[1].split("-")[1])+1))
    if any(i in ele1 for i in ele2) or any(e in ele2 for e in ele1):
        total2 +=1
print(total2)