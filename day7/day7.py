f = open("day7/input.txt", "r")
f_content = f.readlines()

current_dir = []
folders = dict()

def make_folder_unique(current_dict):
    s = ""
    folder_names = []
    for x in current_dir:
        s += x
        folder_names.append(s)
        
    return folder_names

for i in f_content:
    i = i.rstrip()
    if i.startswith("$ cd "):
        dir_name = i.split("$ cd ")[1]
        if dir_name == "..":
            current_dir.pop()
        else:
            # if dir_name not in folders:
            #     folders[dir_name] = 0
            current_dir.append(i.split("$ cd ")[1])
    elif str(i.split()[0]).isnumeric():
        unique_folder = make_folder_unique(current_dir)
        for dir_name in unique_folder:
            if dir_name not in folders:
                folders[dir_name] = 0

        for folder in unique_folder:
            folders[folder] += int(i.split()[0])

#part1
# at_most = [folders[i] for i in folders if folders[i] <= 100000]
# at_most.sort()
# print(sum(at_most))

#part2
size_to_add = 30000000 - (70000000-  folders["/"])
valid_dir = []
for i in folders:
    if folders[i] >  size_to_add:
        valid_dir.append(folders[i])
valid_dir.sort()
print(valid_dir[0])
