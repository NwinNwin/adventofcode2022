f = open("test/test.txt", "r")
f_content = f.readlines()[5:]
table = {1:["N", "Z"], 2:["D", "C", "M"], 3:["P"]}
for i in f_content:
    content = i.rstrip()
    y = content.split("move ")[1].split(" from ")
    content2 = y[1].split(" to ")

    content3 = [int(y[0])] + content2

    content3 = [int(j) for j in content3]
    
    movingstacks = table[content3[1]][:content3[0]]
    table[content3[2]] = movingstacks + table[content3[2]]

    table[content3[1]] = table[content3[1]][content3[0]:]

for key in table:
    print(table[key][0])