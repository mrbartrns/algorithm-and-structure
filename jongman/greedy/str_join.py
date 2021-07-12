import sys
import heapq

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(arr):
    if len(arr) == 1:
        return arr[0]

    answer = 0
    heapq.heapify(arr)
    while len(arr) >= 2:
        # 계속해서 sort가 필요한 경우, heapq 자료구조를 사용한다.
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += a + b
        heapq.heappush(arr, a + b)
    return answer


t = int(si())
for _ in range(t):
    n = int(si())
    arr = list(map(int, si().split()))
    answer = solve(arr)

    print(answer)
