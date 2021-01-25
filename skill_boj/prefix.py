# BOJ 11656
import sys

sys.setrecursionlimit(1500)
si = sys.stdin.readline


def solve(word):
    if not word:
        return ""
    words.append(word)
    solve(word[1:])


words = []
word = si().strip()
solve(word)
words.sort()
print("\n".join(words))