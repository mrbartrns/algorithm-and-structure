# 시각
"""
3이 하나라도 들어가 있는 시각 찾기
-> 문제 해결 아이디어 정리하기
"""
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

cnt = 0
n = int(si())
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) or "3" in str(j) or "3" in str(k):
                cnt += 1
print(cnt)
