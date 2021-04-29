# BOJ 15903
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
cards = list(map(int, si().split()))
heapq.heapify(cards)
k = 0

while k < m:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    value = a + b
    heapq.heappush(cards, value)
    heapq.heappush(cards, value)
    k += 1

print(sum(cards))
