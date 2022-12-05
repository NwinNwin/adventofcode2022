f = open("day5/input.txt", "r")
f_content = f.readlines()[10:]

table = {1:list("SLFZDBRH"), 2:list("RZMBT"), 3: list("SNHCLZ"), 
4: list("JFCS"), 5: list("BZRWHGP"), 
6:list("TMNDGZJV"), 7:list("QPSFWNLG"), 
8:list("RZM"), 9:list("TRVNGLCM")}

#part 1
# for i in f_content:
#     content = i.rstrip()
#     y = content.split("move ")[1].split(" from ")
#     content2 = y[1].split(" to ")

#     content3 = [int(y[0])]
#     content3.extend(content2)
#     content3 = [int(j) for j in content3]
    
#     movingstacks = table[content3[1]][:content3[0]][::-1]
#     table[content3[2]] = movingstacks + table[content3[2]]

#     table[content3[1]] = table[content3[1]][content3[0]:]

# for key in table:
#     print(table[key][0])

#part2
for i in f_content:
    content = i.rstrip()
    y = content.split("move ")[1].split(" from ")
    content2 = y[1].split(" to ")

    content3 = [int(y[0])]
    content3.extend(content2)
    content3 = [int(j) for j in content3]
    
    movingstacks = table[content3[1]][:content3[0]]
    table[content3[2]] = movingstacks + table[content3[2]]

    table[content3[1]] = table[content3[1]][content3[0]:]

for key in table:
    print(table[key][0])