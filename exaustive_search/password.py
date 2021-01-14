import sys


def solve(vow, con, n):
    password = ""
    if vow + con == n:
        if vow >= 1 and con >= 2:
            for i in range(len(selected)):
                password += selected[i]
            password += "\n"
        return password

    for i in range(len(word)):
        if not has_chosen[i]:
            if not selected or selected[-1] < word[i]:
                has_chosen[i] = True
                selected.append(word[i])
                if word[i] in vowels:
                    password += solve(vow + 1, con, n)
                else:
                    password += solve(vow, con + 1, n)
                selected.pop()
                has_chosen[i] = False
    return password


n, m = map(int, sys.stdin.readline().split())
word = list(sys.stdin.readline().split())
word.sort()
vowels = ["a", "e", "i", "o", "u"]
has_chosen = [False] * len(word)
selected = []
print(solve(0, 0, n)[:-1])
