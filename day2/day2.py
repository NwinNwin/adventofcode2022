f = open("input.txt", "r")
f_content = f.readlines()

#A: Rock
#B: Paper
#C: Scissor

#X: Rock
#Y: Paper
#Z: Scissors

#X = A, X < B, X > C
#Y > A, Y = B, Y < C
#Z < A, Z > B, Z = C
total = 0

scoredict = {"X": 0, "Y": 3, "Z":6, "R": 1, "P": 2, "S": 3}


for i in f_content:
    game = i.rstrip().split()
    if game[1] == "X":
        if game[0] == "A":
            total += scoredict[game[1]] + scoredict["S"]
        elif game[0] == "B":
            total += scoredict[game[1]] + scoredict["R"]
        elif game[0] == "C":
            total += scoredict[game[1]] + scoredict["P"]
    elif game[1] == "Y":
        if game[0] == "A":
            total += scoredict[game[1]] + scoredict["R"]
        elif game[0] == "B":
            total += scoredict[game[1]] + scoredict["P"]
        elif game[0] == "C":
            total += scoredict[game[1]] + scoredict["S"]
    elif game[1] == "Z":
        if game[0] == "A":
            total += scoredict[game[1]] + scoredict["P"]
        elif game[0] == "B":
            total += scoredict[game[1]] + scoredict["S"]
        elif game[0] == "C":
            total += scoredict[game[1]] + scoredict["R"]

print(total)