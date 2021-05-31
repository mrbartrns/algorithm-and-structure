"""
재귀 함수
함수가 하는 작업을 조각내어 그 일부를 완벽히 해결하여 부분답을 도출해 낸후, 나머지를 자기 자신에게 넘겨주어 해를 구성

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 작업을 가장 자연스럽게 조각낼 수 있는 방식 찾기
2. 기저사례의 선택
- 더 이상이 탐색이 필요 없이 답을 도출해 낼 수 있는 조건 선택
3. 자기 자신을 완벽하게 해결
- 부분 답을 구성할 수 있는 조건 선택 및 해에 부분 답을 더함
"""


import sys


def solve(numbers, m, arr):
    string = ""  # 조건을 만족하지 못할 때는 빈 스트링 반환하여 정답에 지장없게 함
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr):
                string += " "
        string += "\n"
        return string  # 조건 만족시 즉시 반환
    # 조각낸 조각들을 해결 (요소를 조건에 맞게 추가하는 것 까지가 완벽한 해결임)
    for i in range(len(numbers)):
        if not arr or arr[-1] <= numbers[i]:
            arr.append(numbers[i])
            string += solve(numbers, m, arr)  # 부분답을 합쳐 전체 답으로 만듬
            arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(unsorted_arr)
arr = []
answer = solve(sorted_arr, m, arr)
sys.stdout.write(answer[:-1])