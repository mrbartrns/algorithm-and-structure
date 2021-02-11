# BOJ 2251
import sys
from collections import deque

si = sys.stdin.readline

"""
물병에 물을 담을 수 있는 조건
조건은 따로 없고, 항상 모든 물병에 대해 물을 담을 수 있을 것이라고 생각해야 한다
즉, 물이 있던 없던간에 항상 모든 경우에 대해서 고려를 해야 하며, 따라서 어느 한쪽에 물이 없는 경우에만
정답 배열에 넣으면 된다.
이미 넣은 물은 더이상 큐에 넣지 않도록 체크 배열(2차원 배열)로 만들어 저장하는 과정이 필요하다
"""

a, b, c = map(int, si().split())
# 각 물병의 크기 제한이 200이고, 물의 양은 항상 일정하므로 a, b물병에 대해서만 체크하면 된다
check = [[0 for _ in range(201)] for _ in range(201)]


def bfs(a, b, c):
    que = deque()
    res = []
    # init queue, a와 b값 추가(처음엔 0)
    que.append((0, 0))
    while que:
        a1, b1 = que.popleft()
        c1 = c - a1 - b1

        # 이미 방문한 적이 있다면 건너뛴다.
        if check[a1][b1] == 1:
            continue

        check[a1][b1] = 1

        # 결과 배열에 넣을때에는 a1이 0이거나 b1이 0일때 추가하면 된다 (c에 있다면 둘중 하나는 빔)
        if a1 == 0:
            res.append(c1)

        # 고정된 a1, b1이므로 반복문 내에서 값이 변화하지 않음
        # 1. a -> b로 옮길때 물의 양 변화
        # a, b에 들어있는 물의 양이 합이 b(용량)보다 크다면, 다 옮겨지지 않는다.
        if a1 + b1 > b:
            que.append((a1 + b1 - b, b))
        # 작거나 같을때에는 a가 완전히 비게된다.
        else:
            que.append((0, a1 + b1))

        # 2. a -> c로 옮길 때 물의 양 변화
        if a1 + c1 > c:
            que.append((a1 + c1 - c, b1))  # b의 기존의 물의 양은 변하지 않으므로
        else:
            que.append((0, b1))

        # 3. b -> a
        if b1 + a1 > a:
            que.append((a, b1 + a1 - a))
        else:
            que.append((a1 + b1, 0))

        # 4. b -> c
        if b1 + c1 > c:
            que.append((a1, b1 + c1 - c))
        else:
            que.append((a1, 0))

        # 5. c -> a
        if c1 + a1 > a:
            que.append((a, b1))
        else:
            que.append((a1 + c1, b1))

        # 6. c -> b
        if c1 + b1 > b:
            que.append((a1, b))
        else:
            que.append((a1, b1 + c1))
    res.sort()
    return res


print(bfs(a, b, c))