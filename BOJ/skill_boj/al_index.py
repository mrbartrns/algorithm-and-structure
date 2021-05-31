# BOJ 10809
import sys

si = sys.stdin.readline
so = sys.stdout.write


def solve(word):
    idx = [-1] * 26
    for i in range(len(word)):
        if idx[ord(word[i]) - ord("a")] == -1:
            idx[ord(word[i]) - ord("a")] = i
    return " ".join(list(map(str, idx)))


word = si().strip()
so(solve(word))