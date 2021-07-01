# 110 옮기기
"""
0과 1로 이루어진 문자열에 대하여 사전순으로 정렬(사전순으로 가장 앞에 오는 문자열)
1. 110을 모두 뽑는다
2. 사전순으로 앞으로 정렬하기 위해서는 앞에 0이 있다면 거기에 끼워 넣어서는 안됨
s의 길이가 100만이고 s의 각 원소의 길이가 100만이기 때문에 그리디 알고리즘으로 접근 필요
1이 나오는 동안에는 appendleft하고 이후에 멈춘후 110의 수 만큼 삽입
나머지 스택에 있는 것들을 삽입 -> 원리에 대하여 알아보기
"""
from collections import deque


def solution(s):
    answer = []
    for string in s:
        answer.append(solve(string))
    return answer


def solve(string):
    stack = []
    cnt = 0
    for c in string:
        stack.append(c)
        if len(stack) >= 3 and stack[-1] == "0" and stack[-2] == "1" and stack[-3] == "1":
            cnt += 1
            for _ in range(3):
                stack.pop()
    que = deque()
    while stack:
        if stack[-1] == "1":
            que.appendleft(stack.pop())
        else:
            break
    while cnt:
        que.appendleft("0")
        que.appendleft("1")
        que.appendleft("1")
        cnt -= 1
    while stack:
        que.appendleft(stack.pop())
    return "".join(que)


if __name__ == "__main__":
    s = ["1110", "100111100", "0111111010"]
    print(solution(s))
