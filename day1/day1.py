f = open("input.txt", 'r')
f_content = f.readlines()
content_lists = []
sum_all = []
content_child = []
for i in f_content:
    if i != "\n":
        content_child.append(int(i.split("\n")[0]))
    else:
        content_lists.append(content_child)
        content_child = []
for x in content_lists:
    sum_all.append(sum(x))
sum_all.sort(reverse=True)
print(sum(sum_all[0:3]))