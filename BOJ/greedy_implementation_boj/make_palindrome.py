# BOJ 1213 팰린드롬 만들기
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def check_palindrome(counts):
    arr = []
    odd_count = 0
    for i in range(len(counts)):
        if counts[i] == 0:
            continue
        if counts[i] % 2 == 1:
            odd_count += 1
        if odd_count >= 2:
            return "I'm Sorry Hansoo"
        arr.append((chr(i + ord("A")), counts[i] // 2, 0))
        if counts[i] % 2 > 0:
            arr.append((chr(i + ord("A")), 0, counts[i] % 2))
    arr.sort(key=lambda x: (x[2], x[0]))
    ret = ""
    odd_ret = ""
    for alphabet, m, n in arr:
        if n == 0:
            ret += alphabet * m
        else:
            odd_ret += alphabet * n
    return ret + odd_ret + ret[::-1]


string = si().strip()
alphabet_counts = [0] * 26
for c in string:
    alphabet_counts[ord(c) - ord("A")] += 1
print(check_palindrome(alphabet_counts))
