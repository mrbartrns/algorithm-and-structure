# BOJ 7662
import heapq
import sys

"""
데이터를 삭제할 때 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제
데이터를 삭제하는 연산은 두가지로 구분
1. 우선순위가 가장 높은 것
2. 우선순위가 가장 낮은 것
동일한 정수가 삽입될 수 있으므로 집합 사용 불가
[-5643, 16, 123]
"""

si = sys.stdin.readline
MAX = 1000000 + 1  # 명령어의 갯수만큼 넣기

t = int(si())
for _ in range(t):
    res = []
    max_q = []
    min_q = []
    visited = [False] * MAX
    k = int(si())
    for i in range(k):
        op, num = si().split()
        if op == "I":
            heapq.heappush(max_q, (-int(num), i))
            heapq.heappush(min_q, (int(num), i))
            visited[i] = True
        elif int(num) == 1:
            while max_q and not visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                visited[max_q[0][1]] = False
                heapq.heappop(max_q)
        else:
            while min_q and not visited[min_q[0][1]]:
                heapq.heappop(min_q)
            if min_q:
                visited[min_q[0][1]] = False
                heapq.heappop(min_q)
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    res.append(f'{-max_q[0][0]} {min_q[0][0]}' if max_q and min_q else 'EMPTY')
    print("\n".join(res))
