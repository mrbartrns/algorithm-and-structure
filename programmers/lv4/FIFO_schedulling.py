# 선입선출 스케쥴링
import heapq


def solution(n, cores):
    q = []
    for i in range(len(cores)):
        heapq.heappush(q, (0, i + 1, cores[i]))

    for i in range(n):
        t, idx, core = heapq.heappop(q)
        if i == n - 1:
            return idx
        t += core
        heapq.heappush(q, (t, idx, core))


if __name__ == '__main__':
    n = 50000
    cores = [i for i in range(1, 10001)]
    print(solution(n, cores))
