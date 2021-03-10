import heapq

# 디스크 컨트롤러
def solution(jobs):
    size = len(jobs)
    time = 0
    ans = 0
    q = []
    for i in range(size):
        heapq.heappush(q, (jobs[i][0] + jobs[i][1], jobs[i][1], jobs[i][0]))

    while q:
        compare, cost, start = heapq.heappop(q)
        if start <= ans:
            time += cost
            ans += time - start
        else:
            ans += cost

    return ans // size


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))