# [카카오] 수식 최대화
from itertools import permutations


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2


def get_numbers_and_opers(expression):
    numbers = []
    opers = []
    number = ""
    for c in expression:
        if c in {"*", "-", "+"}:
            numbers.append(int(number))
            opers.append(c)
            number = ""
        else:
            number += c
    numbers.append(int(number))
    return numbers, opers


def solution(expression):
    priorities = list(permutations(["*", "-", "+"]))
    numbers, opers = get_numbers_and_opers(expression)
    answer = 0
    for priority in priorities:
        cur_numbers = numbers[:]
        cur_opers = opers[:]
        for c in priority:
            idx = 0
            while idx < len(cur_opers):
                if cur_opers[idx] == c:
                    result = calculate(cur_numbers[idx], cur_numbers[idx + 1], c)
                    cur_numbers[idx] = result
                    cur_numbers.pop(idx + 1)
                    cur_opers.pop(idx)
                    idx -= 1
                idx += 1
        answer = max(answer, abs(cur_numbers[0]))
    return answer


if __name__ == "__main__":
    expression = "50*6-3*2"
    print(solution(expression))