"""
재귀함수
- 함수가 하는 작업을 조각내어 그 중 하나를 완벽히 해결하여 부분해를 구하고, 나머지를 자기 자신에게 넘겨 해를 반환받아 완전한 해를 구성

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 작업을 가장 자연스럽게 조각낼 수 있는 방식을 선택
2. 기저사례의 선택
- 더 이상의 탐색이 필요없이 부분해를 구할 수 있는 조건을 선택
3. 조각을 완벽하게 해결하는 방법
- 부분해를 받아 완벽한 해를 구성하고 이를 반환

"""
import sys


def solve(arr):
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
            if not arr or arr[-1] <= numbers[i]:
                append_count += 1
                visited.append(numbers[i])
                arr.append(numbers[i])
                string += solve(arr)
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
answer = solve(arr)
sys.stdout.write(answer[:-1])