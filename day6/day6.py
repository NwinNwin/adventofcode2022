f = open("day6/input.txt", "r")
f_content = f.readlines()[0]

#part1
# content = 4
# while True:
#     if len(set(f_content[:4])) != 4:
#         f_content = f_content[1:]
#         content += 1
#     else: 
#         break


content = 14
while True:
    if len(set(f_content[:14])) != 14:
        f_content = f_content[1:]
        content += 1
    else: 
        break
print(content)