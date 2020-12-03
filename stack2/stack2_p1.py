import operator

def get_operator(op: str):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }[op]


OPERATOR = ['(', '+', '-', '*', '/', ')']

def get_eval(op, num1, num2):
    return get_operator(op)(num1, num2)

def forth(string: list) -> int:
    try:
        stack = []
        if len(string) <= 2:
            return 'error'
        else:
            for c in string:
                if c in OPERATOR:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if c == '+':
                        val = num1 + num2
                    elif c == '-':
                        val = num1 - num2
                    elif c == '*':
                        val = num1 * num2
                    elif c == '/':
                        val = num1 // num2
                    stack.append(val)
                elif c == '.':
                    if len(stack) == 0:
                        return 'error'
                    else:
                        res = stack.pop()
                        if len(stack) != 0:
                            return 'error'
                        return res
                else:
                    stack.append(int(c))
            if len(stack) != 0:
                return 'error'
    except:
        return 'error'

# print(forth(['1', '5', '8', '10', '3', '4', '+', '+', '3', '+', '*', '2', '+', '+', '+', '.']))
print(forth(['5', '3', '*', '+', '.']))
# t = int(input())
# for i in range(t):
#     case = [x for x in input().split()]
#     print(f'#{i + 1} {forth(case)}')
