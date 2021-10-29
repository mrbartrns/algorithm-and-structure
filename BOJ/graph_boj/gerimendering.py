# BOJ 17471 게리맨더링
# 개념에 대한 환벽한 숙지가 중요함**
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def check(node, info):
    """
    현재 노드와 브루트포스로 얻어진 노드 toggle 정보를 이용하여
    현재 노드가 1인지 0인지 판단하는 함수
    """
    if (1 << (node - 1)) & info:
        return True
    return False


def bfs(s, info, label):
    que = deque()
    labels[s] = label
    flag = check(s, info)  # 현재 노드의 정보가 True인지 False인지 저장한다.
    que.append(s)
    while que:
        node = que.popleft()
        for nxt in graph[node]:
            if (
                check(nxt, info) == flag and labels[nxt] == 0
            ):  # 현재 노드와 방문할 노드가 동일한 경우에만 방문하도록 한다.
                labels[nxt] = label
                que.append(nxt)


N = int(si())
population = [0] + list(map(int, si().split(" ")))
graph = [[] for _ in range(N + 1)]
answer = INF
for i in range(1, N + 1):
    temp = list(map(int, si().split()))
    graph[i].extend(temp[1:])
for info in range(
    1 << N
):  # 노드 갯수만큼 비트마스킹을 이용하여 구역을 사전 지정한다. 사전 지정한다고 다 가능한 경우가 되는 것은 아니다.
    label_number = 0
    labels = [0] * (N + 1)
    for j in range(1, N + 1):
        if labels[j] == 0:
            label_number += 1
            bfs(j, info, label_number)
    if (
        label_number == 2
    ):  # 라벨 넘버가 2인 경우에만 단 두번의 bfs로 구역을 지정할 수 있다는 뜻이므로 이 경우에만 두개의 구역으로 나눌 수 있다.
        label1 = 0
        label2 = 0
        for i in range(1, N + 1):
            if labels[i] == 1:
                label1 += population[i]
            else:
                label2 += population[i]
        answer = min(answer, abs(label1 - label2))
print(answer if answer < INF else -1)
