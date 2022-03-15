import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_result(count):
    if count > 0:
        return chr(count + ord("A") - 1)
    return "E"


for _ in range(3):
    result = list(map(int, si().strip().split(" ")))
    count = 0
    for c in result:
        if c == 0:
            count += 1
    print(get_result(count))
