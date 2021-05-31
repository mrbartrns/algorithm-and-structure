# BOJ 1713
import sys

si = sys.stdin.readline
n = int(si())
m = int(si())
arr = list(map(int, si().split()))
frame = [[0, 0]] * n  # 시간, 후보
res = [0] * 101
posted = set()
ans = []
for i in range(len(arr)):
    candidate = arr[i]
    res[candidate] += 1
    replace = True
    for j in range(n):
        if frame[j][1] == 0:
            frame[j] = [i, candidate]
            replace = False
            break
        elif frame[j][1] == candidate:
            replace = False
            break
    if replace:
        idx = 0
        recommend = 10001
        for j in range(n):
            if recommend > res[frame[j][1]]:
                idx = j
                recommend = res[frame[j][1]]
            elif recommend == res[frame[j][1]]:
                if frame[idx][0] > frame[j][0]:
                    idx = j
        res[frame[idx][1]] = 0
        frame[idx][0] = i
        frame[idx][1] = candidate

for i in range(n):
    ans.append(frame[i][1])
ans.sort()
print(" ".join(list(map(str, ans))))
