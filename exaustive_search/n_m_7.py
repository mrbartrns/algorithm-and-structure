"""
재귀함수
- 함수가 하는 작업을 조각내어 그중 하나를 자기 자신이 완벽히 해결하여 부분 문제를 도출해 낸 후, 나머지를 자기 자신에게 넘겨주어 최종 답을 도출

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 일을 가장 자연스럽게 조각내는 방식을 찾기
2. 기저사례의 선택
- 더 이상의 탐색 없이 답을 도출해 낼 수 있는 조건 찾기
3. 자기 자신을 완벽히 해결 후 부분 답을 만들 수 있는 방식 선택
- 반환타입 및 조건을 이용하여 부분 답 구성

이 문제에서
1. 문제의 분할
- 요소를 배열에 추가하고 빼는 것이 가장 자연스럽다.
2. 기저사례의 선택
- 조건에 맞게 구성된 배열의 크기가 m이 되면 배열을 스트링으로 반환하고, 그렇지 않으면 ""을 반환한다.
3. 자기 자신의 해결
- 조건 없이 오름차순으로 배열된 요소를 정답 배열에 추가 후, 이를 이용하여 부분답을 도출한다. 그리고 다음 작업을 하기 위해 다시 배열에 요소를 제거한다. (스택)
"""


import sys


def solve(sorted_arr, m, arr):
    string = ""
    # 기저사례의 선택, 부분답을 즉시 반환하여 완전한 답의 일부를 구성
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr):
                string += " "
        string += "\n"
        return string
    for i in range(len(sorted_arr)):
        arr.append(sorted_arr[i])
        string += solve(sorted_arr, m, arr)  # 반환된 부분답을 이용하여 최종 답을 구성
        arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(unsorted_arr)
arr = []
answer = solve(sorted_arr, m, arr)
sys.stdout.write(answer[:-1])