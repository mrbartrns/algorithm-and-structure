# BOJ 12904 A와 B
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

a = list(si().strip())
b = list(si().strip())


while len(b) > len(a):
    if b[-1] == "A":
        b.pop()
    elif b[-1] == "B":
        b.pop()
        b.reverse()

print(1 if a == b else 0)