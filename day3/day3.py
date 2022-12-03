f = open("day3/input.txt", "r")
f_content = f.readlines()

table = {}

#a: 97
#z: 122

#A:65
#Z: 90

num = 1
total = 0

#make table
for i in range(97,123):
    table[chr(i)] = num
    num += 1
for i in range(65,91):
    table[chr(i)] = num
    num += 1


#part 1
for j in f_content:
    line = j.rstrip()
    half = int(len(line)/2)
    first = line[0:half]
    second = line[half:]
    for item in first:
        if item in second:
            total += table[item]
            break

#part2
total2 = 0
for j in range(3,len(f_content)+1,3):
    
    first = f_content[j-3]
    second = f_content[j-2]
    third  = f_content[j-1]
  
    for e in first:
        if e in second and e in third:
            total2 += table[e]
            break

print(total2)

