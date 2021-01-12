"""
재귀함수
- 함수가 하는 작업을 조각내어 일부를 완벽하게 해결하여 부분답을 도출해 낸 후, 나머지를 자기 자신에게 넘겨 전체 답을 도출

재귀함수의 조건
1. 문제의 분할
- 함수가 하는 작업을 가장 자연스럽게 조각내는 방식 찾기
2. 기저사례 탐색
- 더 이상의 탐색없이 부분답을 도출할 수 있는 조건 찾기
3. 조각을 완벽하게 해결하는 방법 찾기
- 부분 해를 반환 받아 전체 해를 구성
"""
import sys

# 조건을 만족하지 못할 경우 빈 스트링을 반환하여 답에 지장 없게 함
# 중복되는 수열을 여러번 출력하면 안됨 (출력 담당이므로 기저 사례에 조건 추가)
# 기저사례를 만족한다면 부분해를 반환
# 기저사례를 만족하면 즉시 부분해를 반환
# 조각의 일부를 해결후 부분해로부터 전체 해를 구성


def solve(flags, arr, visited):
    string = ""
    append_count = 0

    # not in 보다 더 좋은 성능이 필요
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string

    # 지금 이 부분 원리 파악하고 복습하기
    visited.append(-1)
    for i in range(len(numbers)):
        if not flags[i] and (visited[-1] != numbers[i]):
            flags[i] = True
            visited.append(numbers[i])
            append_count += 1
            arr.append(numbers[i])
            string += solve(flags, arr, visited)
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
answer = solve(flags, arr, visited)
sys.stdout.write(answer[:-1])
