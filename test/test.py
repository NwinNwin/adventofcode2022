f = open("test/test.txt", "r")
f_content = f.readlines()

current_dir = []
folders = dict()
for i in f_content:
    i = i.rstrip()
    if i.startswith("$ cd "):
        dir_name = i.split("$ cd ")[1]
        if dir_name == "..":
            current_dir.pop()
        else:
            if dir_name not in folders:
                folders[dir_name] = 0
            current_dir.append(i.split("$ cd ")[1])
    elif str(i.split()[0]).isnumeric():
        for folder in current_dir:
            folders[folder] += int(i.split()[0])

at_most = [folders[i] for i in folders if folders[i] <= 100000]
at_most.sort()
print(sum(at_most))