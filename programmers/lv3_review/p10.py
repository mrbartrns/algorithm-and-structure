# 단어 변환
from collections import deque


def solution(begin, target, words):
    que = deque()
    visited = set()
    visited.add(begin)
    que.append((begin, 0))
    while que:
        word, cnt = que.popleft()
        if word == target:
            return cnt

        for nxt in words:
            if nxt in visited:
                continue
            chk = 0
            for i in range(len(nxt)):
                if nxt[i] != word[i]:
                    chk += 1
                if chk > 1:
                    break
            if chk <= 1:
                visited.add(nxt)
                que.append((nxt, cnt + 1))
    return 0


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))
