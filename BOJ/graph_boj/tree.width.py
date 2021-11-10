# BOJ 2250 트리의 높이와 너비
import sys

sys.setrecursionlimit(100000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def inorder(node, cnt):
    if tree[node][0] != -1:
        inorder(tree[node][0], cnt + 1)
    order[node] = counter[0]
    counter[0] += 1
    depth[node] = cnt
    if tree[node][1] != -1:
        inorder(tree[node][1], cnt + 1)


def dfs(node):
    if node == -1:
        return 0

    if visited[node] > -1:
        return visited[node]

    visited[node] = 0
    visited[node] = max(dfs(tree[node][0]), dfs(tree[node][1])) + 1
    return visited[node]


# initialize
N = int(si())
counter = [1]
tree = [[-1, -1] for _ in range(N + 1)]
depth = [0] * (N + 1)
order = [0] * (N + 1)
indegree = [[INF, 0] for _ in range(N + 1)]
for _ in range(N):
    a, b, c = map(int, si().split(" "))
    tree[a][0] = b
    tree[a][1] = c

visited = [-1] * (N + 1)
for i in range(1, N + 1):
    if visited[i] == -1:
        dfs(i)
root = visited.index(max(visited))
inorder(root, 1)
for i in range(1, N + 1):
    d = depth[i]
    o = order[i]
    indegree[d][0] = min(indegree[d][0], o)
    indegree[d][1] = max(indegree[d][1], o)
answer = 0
max_depth = 0
for i in range(1, N + 1):
    if indegree[i][1] - indegree[i][0] + 1 > answer:
        answer = indegree[i][1] - indegree[i][0] + 1
        max_depth = i
print(max_depth, answer)
