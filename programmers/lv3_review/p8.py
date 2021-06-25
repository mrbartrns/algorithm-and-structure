# 네트워크
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if dfs(i, visited, computers):
            cnt += 1
    return cnt


def dfs(idx, visited, graph):
    if not visited[idx]:
        visited[idx] = True
        for i in range(len(visited)):
            if graph[idx][i] == 0:
                continue
            dfs(i, visited, graph)
        return True
    return False


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
