g_max = {"green": 0, "blue": 0, "red": 0}
sum = 0

for game in open("input.txt"):
    data = game.strip().split(": ")
    values = data[1].replace(";", ",").split(", ")

    for grab in values:
        val = grab.split()
        if int(val[0]) > g_max[val[1]]:
            g_max[val[1]] = int(val[0])

    prod = 1
    for i in g_max:
        prod *= g_max[i]
        g_max[i] = 0

    sum += prod

print(sum)