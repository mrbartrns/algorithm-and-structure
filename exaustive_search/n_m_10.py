"""
재귀함수
- 함수가 하는 작업을 조각내어 그 중 일부를 자기 자신이 완벽히 처리한 후 부분 해를 반환하여 전체 해를 구성

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 작업을 가장 자연스럽게 조각 낼 수 있는 방식을 선택
2. 기저사례의 선택
- 더 이상의 탐색 없이 부분해를 도출해 낼 수 있는 조건 선택
3. 조각을 완벽하게 해결하는 방법 찾기
- 부분해를 받아 전체 해를 구성
"""
import sys


def solve(arr):
    string = ""
    append_count = 0
    # 기저 사례: 더 이상 탐색 할 필요가 없으면 스트링을 반환
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string
    # 다음 스택으로 함수가 넘어갔을 때 구분해주기 위해서 -1을 실행
    visited.append(-1)
    # 본인을 제외하고, 중복없이, 비 내림차순으로 완벽하게 답을 구성하기 위해 다음과 같이 구성
    for i in range(n):
        if not flags[i] and visited[-1] != numbers[i]:
            if not arr or arr[-1] <= numbers[i]:
                flags[i] = True
                visited.append(numbers[i])
                append_count += 1
                arr.append(numbers[i])
                string += solve(arr)
                arr.pop()
                flags[i] = False

    for _ in range(append_count + 1):
        visited.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
numbers = sorted(unsorted_arr)
arr = []
flags = [False for _ in range(len(numbers))]
visited = []
answer = solve(arr)
sys.stdout.write(answer[:-1])
