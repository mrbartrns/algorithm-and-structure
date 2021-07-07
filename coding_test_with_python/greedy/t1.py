# 모험가 길드
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
n = int(si())
team = list(map(int, si().split()))

team.sort()
group = []
cnt = 0
for t in team:
    group.append(t)
    if len(group) >= t:
        group = []
        cnt += 1
print(cnt)
