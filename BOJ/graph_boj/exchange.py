# BOJ 1039 교환
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
# 전체 배열을 visited로 설정할 시 문제가 발생할 수 있음


def bfs(n, k):
    q = deque()
    q.append((str(n), 0))
    visited[0].add(str(n))
    while q:
        string_number, cnt = q.popleft()
        if cnt >= k:
            continue
        for i in range(len(string_number)):
            for j in range(i + 1, len(string_number)):
                list_number = list(string_number)
                list_number[i], list_number[j] = list_number[j], list_number[i]
                if list_number[0] == "0":
                    continue
                if "".join(list_number) not in visited[cnt + 1]:
                    visited[cnt + 1].add("".join(list_number))
                    q.append(("".join(list_number), cnt + 1))


N, K = map(int, si().split(" "))
visited = [set() for _ in range(K + 1)]
answer = -1
bfs(N, K)
for number in visited[K]:
    answer = max(answer, int(number))
print(answer)
