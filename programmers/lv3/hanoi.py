"""
하노이의 탑 복습하기
"""


def solution(n):
    answer = []
    solve(n, 1, 3, 2, answer)
    return answer


def solve(n, from_, to_, via, answer):
    if n == 1:
        answer.append([from_, to_])
        return

    solve(n - 1, from_, via, to_, answer)
    answer.append([from_, to_])
    solve(n - 1, via, to_, from_, answer)


n = 2
print(solution(n))
