# BOJ 9177 단어 섞기
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si().strip())
cnt = 0


def bfs(word1, word2, word3):
    q = deque()
    visited[0][0] = True
    q.append((0, 0))
    while q:
        left, right = q.popleft()
        if left + right == len(word3):
            return True
        if (
            left < len(word1)
            and word1[left] == word3[left + right]
            and not visited[left + 1][right]
        ):
            visited[left + 1][right] = True
            q.append((left + 1, right))
        if (
            right < len(word2)
            and word2[right] == word3[left + right]
            and not visited[left][right + 1]
        ):
            visited[left][right + 1] = True
            q.append((left, right + 1))
    return False


while cnt < N:
    word1, word2, word3 = map(str, si().strip().split(" "))
    visited = [[False for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    cnt += 1
    print(
        "Data set {cnt}: {value}".format(
            cnt=cnt, value="yes" if bfs(word1, word2, word3) else "no"
        )
    )
