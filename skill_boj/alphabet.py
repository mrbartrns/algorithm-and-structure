# BOJ 10808
import sys

si = sys.stdin.readline


def solve(string):
    alphabet = [0] * 26
    for i in range(len(string)):
        alphabet[ord(string[i]) - ord("a")] += 1
    return " ".join(list(map(str, alphabet)))


string = si().strip()
print(solve(string))