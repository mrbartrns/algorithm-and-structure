import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

count = 0
answer = 0
for _ in range(4):
    a, b = map(int, si().strip().split(" "))
    count -= a
    count += b
    answer = max(answer, count)
print(answer)
