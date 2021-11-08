# BOJ 2457 공주님의 정원
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


count = 0

N = int(si())
schedules = []
for _ in range(N):
    a, b, c, d = map(int, si().split(" "))
    schedules.append((100 * a + b, 100 * c + d))
schedules.sort(key=lambda x: x[0])
current_idx = 301
search_idx = 0
count = 0
while current_idx <= 1130:
    new_end_time = 0
    for i in range(N):
        start_time, end_time = schedules[i]
        if current_idx >= start_time:
            if new_end_time < end_time:
                new_end_time = end_time
        else:
            break
    if new_end_time == 0:
        break
    else:
        current_idx = new_end_time
        count += 1

print(count if current_idx > 1130 else 0)
