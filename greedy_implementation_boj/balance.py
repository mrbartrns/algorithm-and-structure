# BOJ 4949
import sys

si = sys.stdin.readline


def solve(string):
    stack = []
    for c in string:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
    return True if not stack else False


while True:
    string = si().rstrip()
    if string == ".":
        break
    print("yes") if solve(string) else print("no")
