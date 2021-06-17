# BOJ 17609 (유사 팰린드롬)
import sys

sys.setrecursionlimit(100000)
sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(word, chk):
    if len(word) <= 1 and chk:
        return 0
    elif len(word) <= 1 and not chk:
        return 1

    if word[0] != word[-1] and chk:
        chk = False
        ans = 2
        if len(word) >= 2 and word[1] == word[-1]:
            ans = min(ans, solve(word[2:-1], chk))
        if len(word) >= 2 and word[0] == word[-2]:
            ans = min(ans, solve(word[1: -2], chk))
        return ans
    elif word[0] != word[-1]:
        return 2
    return solve(word[1:-1], chk)


n = int(si())
for _ in range(n):
    word = si().strip()
    print(solve(word, True))

word = "comwwtmoc"
print(solve(word, True))
