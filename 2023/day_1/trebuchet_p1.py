sum = 0

for word in open("p_input.txt"):
    digits = [ch for ch in word if ch.isdigit()]
    sum += int(digits[0] + digits[-1])

print(sum)