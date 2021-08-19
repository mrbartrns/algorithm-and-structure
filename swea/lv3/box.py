# SWEA 5658 보물상자 비밀번호
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def get_number(number):
    ret = 0
    for i in range(len(number)):
        res = check(number[i])
        ret += 16 ** (len(number) - 1 - i) * res
    return ret


def check(c):
    if "0" <= c <= "9":
        return int(c)

    return ord(c) - ord('A') + 10


t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    que = deque(list(input().strip()))
    s = set()
    for _ in range(n):
        for i in range(4):
            left = i * (n // 4)
            right = (i + 1) * (n // 4)
            number = ''
            for j in range(left, right):
                number += que[j]
            int_number = get_number(number)
            s.add(int_number)
        que.rotate(1)
    arr = list(s)
    arr.sort(key=lambda x: -x)
    answer = arr[k - 1]
    print(f'#{tc + 1} {answer}')
