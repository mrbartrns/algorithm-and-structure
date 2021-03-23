# BOJ 2475
import sys
from functools import reduce

si = sys.stdin.readline

arr = list(map(int, si().split()))
val = reduce(lambda acc, cur: acc + cur ** 2, arr, 0) % 10
print(val)