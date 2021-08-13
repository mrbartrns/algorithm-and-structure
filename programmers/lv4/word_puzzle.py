# 단어 퍼즐
import sys

sys.setrecursionlimit(20001)
INF = 987654321


def solution(strs, t):
    words = [[] for _ in range(26)]
    for c in strs:
        words[ord(c[0]) - ord('a')].append(c)
    answer = backtrack(0, '', t, words)
    return answer if answer < INF else -1


def backtrack(cnt, my_word, t, words):
    answer = INF
    if my_word == t:
        return cnt

    if len(my_word) >= len(t):
        return answer

    start = ord(t[len(my_word)]) - ord('a')
    if not words[start]:
        return answer

    for component in words[start]:
        if len(component) + len(my_word) > len(t):
            continue
        for i in range(len(component)):
            if component[i] != t[len(my_word) + i]:
                break
            answer = min(answer, backtrack(cnt + 1, my_word + component, t, words))
    return answer


if __name__ == '__main__':
    strs = ["ba", "an", "nan", "ban", "n"]
    t = "banana"
    print(solution(strs, t))
