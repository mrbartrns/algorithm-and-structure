# BOJ 10799
import sys

si = sys.stdin.readline


def solve(string):
    stack = []
    cnt = 0
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if string[i - 1] == "(":
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    return cnt


string = si().strip()
print(solve(string))