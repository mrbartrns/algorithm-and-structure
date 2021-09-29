# [카카오] 수식 최대화
from itertools import permutations


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2


def separate(expression):
    numbers = []
    ops = []
    t = ""
    for c in expression:
        if c in {"+", "-", "*"}:
            numbers.append(int(t))
            t = ""
            ops.append(c)
        else:
            t += c
    numbers.append(int(t))
    return numbers, ops


def solution(expression):
    answer = 0
    numbers, ops = separate(expression)
    priorities = list(permutations(["+", "-", "*"]))
    for priority in priorities:
        numbers_copy = numbers[:]
        ops_copy = ops[:]
        for i in range(3):
            idx = 0
            while idx < len(ops_copy):
                if ops_copy[idx] == priority[i]:
                    numbers_copy[idx] = calculate(
                        numbers_copy[idx], numbers_copy[idx + 1], ops_copy[idx]
                    )
                    numbers_copy.pop(idx + 1)
                    ops_copy.pop(idx)
                    idx -= 1
                idx += 1
        answer = max(answer, abs(numbers_copy[0]))
    return answer


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))