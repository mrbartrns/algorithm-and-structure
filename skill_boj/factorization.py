# BOJ 11653
import sys

input = sys.stdin.readline


def divide(n):
    string = ""
    if n == 1:
        return ""
    for i in range(2, n + 1):
        if n % i == 0:
            string = str(i) + " " + divide(n // i)
            break
    return string


n = int(input())
if n > 1:
    string = divide(n).strip()
    arr = sorted(map(int, string.split(" ")))
    print("\n".join(map(str, arr)))
# print(string.split(" "))