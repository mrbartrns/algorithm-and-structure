# SWEA 12221 구구단
import sys

sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def is_over_10(a, b):
    if a >= 10:
        return True
    if b >= 10:
        return True
    return False


t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    answer = a * b if not is_over_10(a, b) else -1
    print(f'#{tc + 1} {answer}')
