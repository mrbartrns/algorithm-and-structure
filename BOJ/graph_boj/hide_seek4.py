# BOJ 13913 숨바꼭질
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def bfs(start):
    q = []
    visited[start] = start
    heapq.heappush(q, (0, start))
    while q:
        cnt, node = heapq.heappop(q)
        if node == K:
            return cnt
        if node * 2 <= 200000 and visited[node * 2] == INF:
            visited[node * 2] = node
            heapq.heappush(q, (cnt + 1, node * 2))
        if node + 1 <= 200000 and visited[node + 1] == INF:
            visited[node + 1] = node
            heapq.heappush(q, (cnt + 1, node + 1))
        if node - 1 >= 0 and visited[node - 1] == INF:
            visited[node - 1] = node
            heapq.heappush(q, (cnt + 1, node - 1))


# visited 에다가 노드 번호 집어넣기
N, K = map(int, si().split(" "))
visited = [INF] * 200001
ret = []
print(bfs(N))
st = K
while visited[st] != st:
    ret.append(st)
    st = visited[st]
ret.append(st)
ret.reverse()
print(" ".join(list(map(str, ret))))
