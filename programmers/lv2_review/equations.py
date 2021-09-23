# [카카오] 수식 최대화
from itertools import permutations


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2


def get_ops_and_numbers(expression):
    ops = []
    numbers = []
    number = ""
    for c in expression:
        if c in {"*", "-", "+"}:
            numbers.append(int(number))
            ops.append(c)
            number = ""
        else:
            number += c
    numbers.append(int(number))
    return ops, numbers


def solution(expression):
    answer = 0
    # ops -> 여러개의 opers
    ops, numbers = get_ops_and_numbers(expression)
    priorities = list(permutations(["*", "-", "+"]))
    for priority in priorities:
        ops_copy = ops[:]
        numbers_copy = numbers[:]
        for c in priority:
            i = 0
            while i < len(ops_copy):
                if ops_copy[i] == c:
                    ret = calculate(numbers_copy[i], numbers_copy[i + 1], ops_copy[i])
                    numbers_copy[i] = ret
                    numbers_copy.pop(i + 1)
                    ops_copy.pop(i)
                    i -= 1
                i += 1
        answer = max(answer, abs(numbers_copy[0]))
    return answer


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))