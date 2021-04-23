# BOJ 2217
"""
k개의 로프를 사용하여 최대 중량이 w / k 만큼 들 수 있을때 들을 수 있는 최대 중량
모든 로프를 사용해야 할 필요가 없으며 임의로 몇개의 로프를 골라서 사용해도 괜찮음
"""
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline


n = int(si())
arr = []
for _ in range(n):
    arr.append(int(si()))

arr.sort(reverse=True)
res = 0
for i in range(n):
    res = max(res, arr[i] * (i + 1))

print(res)
