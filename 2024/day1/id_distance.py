
def calculate_distance():
    list_a = []
    list_b = []
    for id in open("input1.txt"):
        a, b = id.split()
        list_a.append(int(a))
        list_b.append(int(b))

    list_b.sort()
    list_a.sort()

    total = 0
    for i in range(len(list_a)):
        total += abs(int(list_a[i]) - int(list_b[i]))
    print(total)


def calculate_score():
    list_a = []
    list_b = {}

    for id in open("input1.txt"):
        a, b = id.split()
        if int(b) in list_b:
            list_b[int(b)] += 1
        else:
            list_b[int(b)] = 1
        list_a.append(int(a))

    score = 0
    for id in list_a:
        if id in list_b:
            score += id * list_b[id]
    print(score)


if __name__ == "__main__":
    calculate_distance()
    calculate_score()
