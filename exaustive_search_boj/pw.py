# BOJ 1759
import sys

si = sys.stdin.readline


def backtrack(word, con, vow):
    if len(word) == l:
        if con >= 2 and vow >= 1:
            print("".join(word))
        return

    for i in range(c):
        if (not visited[i]) and (not word or word[-1] < alphabets[i]):
            visited[i] = True
            word.append(alphabets[i])
            if alphabets[i] in vowels:
                backtrack(word, con, vow + 1)
            else:
                backtrack(word, con + 1, vow)
            word.pop()
            visited[i] = False


l, c = map(int, si().split())
alphabets = si().split()
alphabets.sort()
vowels = set(["a", "e", "i", "o", "u"])
visited = [False] * c
word = []
backtrack(word, 0, 0)