# BOJ 1173
import sys

si = sys.stdin.readline

N, m, M, T, R = map(int, si().split())  # 운동시간, 초기 맥박, 최대 맥박, 맥박 증가량, 맥박 감소량
time = 0
exercise = 0
check = True
cur = m

if m + T > M:
    print(-1)
    sys.exit(0)

while exercise < N:
    if cur + T <= M:
        exercise += 1
        cur += T
    else:
        if cur - R >= m:
            cur -= R
        else:
            cur = m
    time += 1

print(time)
