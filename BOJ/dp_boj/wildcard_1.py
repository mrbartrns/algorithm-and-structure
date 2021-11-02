# 와일드카드
# 와일드 카드 문제 계속 복습하기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def match_memoized(w, s):
    if cache[w][s] > -1:
        return cache[w][s]

    cache[w][s] = 0
    while w < len(W) and s < len(S) and (W[w] == S[s] or W[w] == "?"):
        w += 1
        s += 1

    if w == len(W):
        cache[w][s] = 1 if s == len(S) else 0
        return cache[w][s]

    if W[w] == "*":
        for skip in range(len(S) - s + 1):
            if match_memoized(w + 1, s + skip):
                cache[w][s] = 1
                return cache[w][s]
    return cache[w][s]


def match_memoized_optimized(w, s):
    """
    만약 재귀 함수 내부에 반복문이 하나도 존재하지 않도록 바꾼다면
    부분 문제 개수와 같은 시간만을 사용해 해결이 가능하다.
    """

    if cache[w][s] > -1:
        return cache[w][s]

    if w == len(W):
        cache[w][s] = 1 if s == len(S) else 0
        return cache[w][s]
    # while문을 통과했다는 뜻은 W[w] == S[s]가 서로 대응된다는 뜻이다.
    # 이때 w와 s를 1씩 증가하고 계속하는 대신에, 패턴의 문자열을 떼고 이들이 대응되는지 확인한다.
    cache[w][s] = 0
    if w < len(W) and s < len(S) and (W[w] == "?" or W[w] == S[s]):
        cache[w][s] = match_memoized_optimized(w + 1, s + 1)
    if W[w] == "*":
        if match_memoized_optimized(w + 1, s) or (
            s < len(S) and match_memoized_optimized(w, s + 1)
        ):
            cache[w][s] = 1
            return cache[w][s]
    return cache[w][s]


T = int(si())
for _ in range(T):
    W = si().strip()
    N = int(si())
    for _ in range(N):
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        S = si().strip()
        if match_memoized_optimized(0, 0):
            print(S)
