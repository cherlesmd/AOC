import re
sum = 0

for game in open("input.txt"):
    values = game.strip().split(": ")
    cubes = values[1].replace(";", ",").split(", ")
    valid = True

    for grab in cubes:
        v = grab.split()

        if int(v[0]) > 14:
            valid = False
            break

        elif int(v[0]) > 12 and v[1] == "red":
            valid = False
            break

        elif int(v[0]) == 14 and v[1] == "green":
            valid = False
            break
        
    if valid == True:
        sum += int(values[0].split(" ")[1])

print(sum)