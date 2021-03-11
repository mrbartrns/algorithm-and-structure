# 네트워크
def solution(n, computers):
    def dfs(i):
        if not visited[i]:
            visited[i] = True
            for j in range(n):
                if computers[i][j] == 1:
                    dfs(j)
            return True
        return False

    answer = 0
    visited = [False] * n
    for i in range(n):
        if dfs(i):
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))