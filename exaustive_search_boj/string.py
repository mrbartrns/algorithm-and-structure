# BOJ 1120
import sys


si = sys.stdin.readline

# 모든 글자 추가 가능

MIN = 51


a, b = map(str, si().split())
res = MIN
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if b[i + j] != a[j]:
            cnt += 1
    res = min(res, cnt)
print(res)


"""
def solve(string):
    if len(string) == size:
        s = 0
        for i in range(size):
            if string[i] != b[i]:
                s += 1
        cnt[0] = min(cnt[0], s)
        return
    for i in range(26):
        if alphabets[i]:
            solve(chr(ord("a") + i) + string)
            solve(string + chr(ord("a") + i))
"""
"""
def bfs(string):
    que = deque()
    que.append(string)
    res = MIN
    while que:
        s = que.popleft()
        if len(s) == size:
            cnt = 0
            for i in range(size):
                if b[i] != s[i]:
                    cnt += 1
            res = min(res, cnt)
        elif len(s) < size:
            for i in range(26):
                alpha = chr(ord("a") + i)
                if alphabets[i]:
                    que.append(s + alpha)
                    que.append(alpha + s)
    return res
"""