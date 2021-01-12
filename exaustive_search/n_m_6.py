"""
재귀함수
- 문제를 이루는 여러 조각들 중 하나를 떼내어 자기자신이 완벽히 해결하여 부분 문제의 답을 이룬 후, 자기 자신을 호출하여 나머지를 해결

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 일을 가장 자연스럽게 조각낼 수 있는 방식 찾기
2. 기저사례의 선택
- 더 이상의 탐색 없이 답을 도출해 낼 수 있는 조건 선택 (조건은 여러개가 될 수 있음)
3. 자기 자신을 완벽하게 해결하는 방법을 선택
- 반환타입 고려


이 문제에서
1. 문제의 분할
- 정답 배열에 요소를 추가, 다시 반환되면 요소를 제거
2. 기저사례의 선택
- 정답 배열의 길이가 n이 될때, 탐색을 멈춤 (즉시 반환)
3. 자기 자신의 완벽한 해결 및 부분답 도출
- 요소를 추가시 정답 배열의 마지막 요소보다 작다면 요소를 추가하지 않음 (아무 작업도 하지 않음)
"""
import sys


def solve(sorted_arr, m, arr):
    string = ""
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string
    for i in range(len(sorted_arr)):
        if not arr or arr[-1] < sorted_arr[i]:
            arr.append(sorted_arr[i])
            string += solve(sorted_arr, m, arr)
            arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(unsorted_arr)
arr = []
answer = solve(sorted_arr, m, arr)
sys.stdout.write(answer[:-1])