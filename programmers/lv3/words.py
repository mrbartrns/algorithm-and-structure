# 단어 변환
from collections import deque


def solution(begin, target, words):
    visited = set()
    que = deque([(begin, 0)])
    while que:
        word, cnt = que.popleft()
        if word == target:
            return cnt
        for new in words:
            temp = 0
            if new in visited:
                continue
            for i in range(len(new)):
                if new[i] != word[i]:
                    temp += 1
                if temp > 1:
                    break
            else:
                visited.add(new)
                que.append((new, cnt + 1))
    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))