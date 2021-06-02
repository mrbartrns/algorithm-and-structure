# 110 옮기기
from collections import deque


def solution(s):
    answer = []
    for string in s:
        stack = []
        number = 0
        for i in range(len(string)):
            stack.append(string[i])
            if stack[-1] == "0":
                if (
                        len(stack) >= 3
                        and stack[-1] == "0"
                        and stack[-2] == "1"
                        and stack[-3] == "1"
                ):
                    for j in range(3):
                        stack.pop()
                    number += 1
        res = deque()
        while stack:
            if stack[-1] == "1":
                res.appendleft(stack.pop())
            else:
                break
        while number > 0:
            res.appendleft("0")
            res.appendleft("1")
            res.appendleft("1")
            number -= 1
        while stack:
            res.appendleft(stack.pop())
        answer.append("".join(res))
    return answer


if __name__ == "__main__":
    s = ["1110", "100111100", "0111111010"]
    print(solution(s))
