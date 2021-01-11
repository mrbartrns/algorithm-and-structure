import operator

"""
    1. make ISP and ICP table
"""


def get_operator(op: str):
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }[op]


ISP = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}

ICP = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 3}

OPERATOR = ["(", "+", "-", "*", "/", ")"]


def postfix(string: str) -> list:
    stack = []
    res = []
    temp = ""
    for c in string:
        if c in OPERATOR:
            if temp:
                res.append(temp)
                temp = ""
            if c == ")":
                while stack:
                    op = stack.pop()
                    if op == "(":
                        break
                    else:
                        res.append(op)
            else:
                while ICP[c] <= (ISP[stack[-1]] if stack != [] else -1):
                    op = stack.pop()
                    res.append(op)
                stack.append(c)
        else:
            temp += c
    while stack:
        op = stack.pop()
        res.append(op)

    return res


def get_eval(op, num1, num2):
    return get_operator(op)(num1, num2)


def calc(arr: list) -> int or float:
    stack = []
    for c in arr:
        if c not in OPERATOR:
            stack.append(int(c))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            val = get_eval(c, num1, num2)
            stack.append(val)
    res = stack.pop()
    return int(res) if int(res) == float(res) else float(res)


# print(calc(postfix('(6+5*(2-8)/2)')))
print(postfix("(6+5*(2-8)/2)"))
