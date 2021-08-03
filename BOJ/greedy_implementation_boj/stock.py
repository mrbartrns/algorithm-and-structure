import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


t = int(si())
for _ in range(t):
    n = int(si())
    arr = list(map(int, si().split()))
    answer = 0
    max_value = 0
    for s in arr[::-1]:
        if s <= max_value:
            answer += max_value - s
        else:
            max_value = s
    print(answer)