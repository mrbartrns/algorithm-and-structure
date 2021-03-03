# 수식 최대화
import re
from itertools import permutations


def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == "*":
        res = eval("*".join([calc(priority, n + 1, e) for e in expression.split("*")]))
    if priority[n] == "+":
        res = eval("+".join([calc(priority, n + 1, e) for e in expression.split("+")]))
    if priority[n] == "-":
        res = eval("-".join([calc(priority, n + 1, e) for e in expression.split("-")]))
    return str(res)


def solution(expression):
    priorities = list(permutations(["*", "-", "+"]))
    ans = 0
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        ans = max(ans, abs(res))
    return ans


expression = "100-200*300-500+20"
print(solution(expression))