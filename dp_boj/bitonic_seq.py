import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                memo_sec[i] = max(memo_sec[i], memo_sec[j] + 1)
            if seq_re[i] > seq_re[j]:
                memo_sec_re[i] = max(memo_sec_re[i], memo_sec_re[j] + 1)
    memo_sec_re.reverse()
    memo = [memo_sec[i] + memo_sec_re[i] for i in range(n)]
    return max(memo) - 1


"""
n = 10
sequence = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
seq_re = sequence[:]
seq_re.reverse()
memo_sec = [1] * n
memo_sec_re = [1] * n
# solve(n)
print(solve(n))
"""
n = int(input())
sequence = list(map(int, input().split()))
seq_re = sequence[:]
seq_re.reverse()
memo_sec = [1] * n
memo_sec_re = [1] * n
print(solve(n))