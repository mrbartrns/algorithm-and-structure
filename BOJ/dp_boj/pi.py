# 원주율 외우기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def get_score(word):
    if len(word) < 3:
        return INF
    same_number = True
    pattern = True
    seq = True
    seq1 = True
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            pattern = False
            seq = False
            seq1 = False
        elif i - 2 >= 0 and word[i] == word[i - 2]:
            same_number = False
            seq = False
            seq1 = False
        elif i - 2 >= 0 and int(word[i]) - int(word[i - 1]) == int(word[i - 1]) - int(
            word[i - 2]
        ):
            same_number = False
            pattern = False
            if abs(int(word[i]) - int(word[i - 1])) == 1:
                seq = False
            else:
                seq1 = False
        elif i - 2 >= 0:
            same_number = False
            pattern = False
            seq = False
            seq1 = False
    if same_number:
        return 1
    if seq1:
        return 2
    if pattern:
        return 4
    if seq:
        return 5
    return 10


def pi_scores(idx):
    if idx > len(digits):
        return 0
    if cache[idx] > -1:
        return cache[idx]
    cache[idx] = INF
    for i in range(3, 6):
        word = digits[idx : idx + i]
        cache[idx] = min(cache[idx], get_score(word) + pi_scores(idx + i))
    return cache[idx]


T = int(si())
for _ in range(T):
    digits = si().strip()
    cache = [-1] * 10001
    print(pi_scores(0))
