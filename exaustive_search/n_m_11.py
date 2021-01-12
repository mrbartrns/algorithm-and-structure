"""
재귀함수
- 함수가 하는 작업을 조각 내어 그중 하나에 대해 완벽한 부분해를 구하고, 나머지를 자기 자신으로 넘겨 완전한 해를 만드는 함수

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 작업을 가장 자연스럽게 조각낼 수 있는 방식을 선택
2. 기저사례의 선택
- 더 이상의 탐색이 필요 없이 부분해를 구할 수 있는 조건을 선택
3. 조각을 완벽하게 해결하는 방법 찾기
- 완벽하게 조각을 해결하고 부분해를 반환받아 완전한 해 도출
"""
import sys

# 어떻게 하면 중복으로 입력받는 것을 방지 할 수 있는지에 대해 생각하기
def solve(arr, visited):
    string = ""
    append_count = 0
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string

    visited.append(-1)
    for i in range(n):
        if visited[-1] != numbers[i]:
            visited.append(numbers[i])
            arr.append(numbers[i])
            append_count += 1
            string += solve(arr, visited)
            arr.pop()
    for _ in range(append_count + 1):
        visited.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
arr = []
flags = [False for _ in range(len(numbers))]
visited = []
answer = solve(arr, visited)
sys.stdout.write(answer[:-1])