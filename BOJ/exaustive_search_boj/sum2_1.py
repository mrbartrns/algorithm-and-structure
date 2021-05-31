# BOJ 2003
import sys

si = sys.stdin.readline


# 투포인터 알고리즘을 이용한 문제 해결 방식
"""
N칸의 1차원 배열이 있을 때, 부분 배열중 그 원소의 합이 M이 되는 경우의 수를 구하기

포인터 두개를 준비 (start, end 또는 left, right)
맨 처음에는 start = end = 0, start <= end를 항상 만족해야함
현재 부분 배열의 시작과 끝을 가리키는 역할
s = e 일 경우 크기가 0 인 아무것도 포함하지 않는 부분배열을 뜻한다.
start < n인 동안 이 과정을 반복
1. 현재 부분합이 M 이상이거나, 이미 end = N이면 start++
2. 그렇지 않다면, end++
3. 현재 부분합이 M과 같다면, count++
"""


def solve(n, m, arr):
    start = end = cnt = s = 0
    while start < n:
        if s >= m:
            s -= arr[start]
            start += 1
        elif end == n:
            break
        else:
            s += arr[end]
            end += 1

        if s == m:
            cnt += 1
    return cnt


n, m = map(int, si().split())
seq = list(map(int, si().split()))
print(solve(n, m, seq))