"""
그리디(스택) 방식으로 문제 해결하기
k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
"""


def solution(number: str, k: int):
    stack = []
    cnt = k

    for c in number:
        while cnt > 0 and stack and int(stack[-1]) < int(c):
            stack.pop()
            cnt -= 1
        stack.append(c)

    while cnt > 0 and stack:
        stack.pop()
        cnt -= 1

    return "".join(stack)


number = "4177252841"
k = 4
print(solution(number, k))
