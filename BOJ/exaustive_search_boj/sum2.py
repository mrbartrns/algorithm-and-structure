# BOJ 2003
import sys

si = sys.stdin.readline
sys.setrecursionlimit(1000000)
"""
수열의 i번째 수부터 j번째 수 까지의 합이 M이 되는 경우

"""

# dfs를 이용할 시 메모리초과가 발생


def dfs(idx, cnt, s):
    if idx + cnt == n:
        return

    if s + seq[idx + cnt] == m:
        counts[0] += 1
        dfs(idx + 1, 0, 0)
    elif s + seq[idx + cnt] < m:
        dfs(idx, cnt + 1, s + seq[idx + cnt])
    else:
        dfs(idx + 1, 0, 0)


n, m = map(int, si().split())
seq = list(map(int, si().split()))
counts = [0]
dfs(0, 0, 0)
print(counts[0])