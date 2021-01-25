# BOJ 9012
import sys

si = sys.stdin.readline


def is_vps(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(string[i])

    if not stack:
        return True
    return False


n = int(si())
for _ in range(n):
    string = si().strip()
    if is_vps(string):
        print("YES")
    else:
        print("NO")