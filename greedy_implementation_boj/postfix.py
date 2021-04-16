# BOJ 1918
import sys

si = sys.stdin.readline

string = si().strip()
res = ""
stack = []

for c in string:
    if ord('A') <= ord(c) <= ord('Z'):
        res += c
    else:
        if c == "(":
            stack.append(c)
        elif c == "*" or c == "/":
            while stack and (stack[-1] == "/" or stack[-1] == "*"):
                res += stack[-1]
                stack.pop()
            stack.append(c)
        elif c == "+" or c == "-":
            while stack and stack[-1] != "(":
                res += stack[-1]
                stack.pop()
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                res += stack[-1]
                stack.pop()
            stack.pop()

while stack:
    res += stack[-1]
    stack.pop()
print(res)
