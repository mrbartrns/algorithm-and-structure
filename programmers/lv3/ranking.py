def solution(n, results):
    answer = 0
    win = [set() for _ in range(n + 1)]
    lose = [set() for _ in range(n + 1)]
    # make win graph and lose graph
    for i in range(len(results)):
        w, l = results[i]
        win[w].add(l)
        lose[l].add(w)

    for i in range(1, n + 1):
        true_cnt = 0
        visited = [False for _ in range(n + 1)]
        dfs(i, win, visited)
        dfs(i, lose, visited)
        for j in range(1, n + 1):
            if visited[j]:
                true_cnt += 1
        if true_cnt == n:
            answer += 1
    return answer


def dfs(idx, arr, visited):
    visited[idx] = True
    for v in arr[idx]:
        if not visited[v]:
            dfs(v, arr, visited)


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))
