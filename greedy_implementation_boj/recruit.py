# BOJ 1946
"""
A의 성적이 다른 지원자 B의 성적에 비해 둘다 떨어질 경우, 선발 X
주어지는 입력은 성적의 '순위'임. 숫자가 낮을수록 성적이 높음
"""
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    n = int(si())
    arr = []
    val = 1
    for _ in range(n):
        a, b = map(int, si().split())
        arr.append((a, b))
    arr.sort(key=lambda x: (x[0], x[1]))
    score = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < score:
            score = arr[i][1]
            val += 1
    print(val)
