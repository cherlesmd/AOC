import re

sum = 0
spelled = "one two three four five six seven eight nine".split()
# ?= positive lookahead, find any in spelled or any digit
pattern  = "(?=(" + "|".join(spelled) + "|\\d))"

def f(x):
    if x in spelled:
        return str(spelled.index(x) + 1)
    return x

for word in open("p_input.txt"):
    digits = [*map(f, re.findall(pattern, word))]
    sum += int(digits[0] + digits[-1])

print(sum)