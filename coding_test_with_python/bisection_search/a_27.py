# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, x = map(int, si().split())
arr = list(map(int, si().split()))
answer = bisect_right(arr, x) - bisect_left(arr, x)
print(answer if answer > 0 else -1)
