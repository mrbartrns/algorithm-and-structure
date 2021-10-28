# BOJ 13413 오셀로 재배치
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    count = 0
    N = int(si())
    before = si().strip()
    after = si().strip()
    wdiff, bdiff = 0, 0
    for i in range(N):
        if before[i] == "W" and after[i] == "B":
            wdiff += 1
        elif before[i] == "B" and after[i] == "W":
            bdiff += 1
    print(max(wdiff, bdiff))
