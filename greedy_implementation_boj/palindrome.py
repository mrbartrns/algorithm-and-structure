# BOJ 1259
import sys

si = sys.stdin.readline
# used dynamic programming paradime
"""
while 1:
    string = si().strip()
    if string == "0":
        break
    arr = [""] + list(string)
    n = len(string)
    dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n - 1, 0, -1):
        for j in range(n, 1, -1):
            if j > i:
                dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else 0
    print("yes" if dp[1][n] else "no")
"""

# recursion
def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


while 1:
    string = si().strip()
    if string == "0":
        break
    print("yes" if is_palindrome(string) else "no")