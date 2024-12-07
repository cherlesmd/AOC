import numpy as np


def find_safe_reports():
    total = 0
    for line in open("input.txt"):
        levels = [int(level) for level in line.split()]
        total += examine_diffs(levels)

    return total


def find_dampened_safe_report():
    total = 0
    for line in open("input.txt"):
        levels = [int(level) for level in line.split()]

        diffs = np.diff(levels)
        diff_of_diffs = np.all(diffs >= 1) and np.all(diffs <= 3)
        diff_of_diffs2 = np.all(diffs <= -1) and np.all(diffs >= -3)

        if not (diff_of_diffs) or not (diff_of_diffs2):
            for level in range(len(levels)):
                if examine_diffs(np.delete(levels, level)) == 1:
                    total += 1
                    break
        else:
            total += 1

    return total


def examine_diffs(levels):
    diffs = np.diff(levels)

    diff_of_diffs = np.all(diffs >= 1) and np.all(diffs <= 3)
    diff_of_diffs2 = np.all(diffs <= -1) and np.all(diffs >= -3)

    if diff_of_diffs or diff_of_diffs2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(find_safe_reports())
    print(find_dampened_safe_report())
