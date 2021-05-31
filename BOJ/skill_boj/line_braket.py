# BOJ 10799
import sys

si = sys.stdin.readline


def get_count(string):
    stack = []
    res = 0
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")" and string[i - 1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
    return res


string = si().strip()
print(get_count(string))