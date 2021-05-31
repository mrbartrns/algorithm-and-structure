# BOJ 10804
import sys

si = sys.stdin.readline

cards = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, si().split())
    for i in range((b - a + 1) // 2):
        cards[a + i], cards[b - i] = cards[b - i], cards[a + i]

for i in range(1, 21):
    print(cards[i], end=" ")
