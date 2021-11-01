"""
dp문제 접근 방법
1. 먼저 완전탐색의 형식으로 구현하기
2. 반복되는 부분을 메모이제이션
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def match(w, s):
    pos = 0
    while (pos < len(w) and pos < len(s)) and (w[pos] == "?" or w[pos] == s[pos]):
        pos += 1

    # 1. pos == len(w) 일 때 * 문자를 하나도 포함하고 있지 않으므로
    # 모든 글자가 일치해야 한다.
    if pos == len(w):
        return pos == len(s)

    # 2. w[pos] == '*'일 때 문자를 쪼개야 한다.
    # 얼마만큼 쪼갤지는 완전탐색으로 결정한다.
    if w[pos] == "*":
        for skip in range(len(s) - pos + 1):
            if match(w[pos + 1 :], s[pos + skip :]):
                return True
    return False


T = int(si())
for _ in range(T):
    wild = si().strip()
    N = int(si())
    for _ in range(N):
        string = si().strip()
        if match(wild, string):
            print(string)
