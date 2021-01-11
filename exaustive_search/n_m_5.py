"""
1. 어떤것을 분할하여 반복할 지
- 배열에 리스트를 추가하기
2. 기저사례
- 배열의 크기가 m일때, 스트링을 반환
3. 어디까지 해결후 답의 일부를 만들지
- 조건에 맞추어 배열을 리스트에 추가 후, 함수를 호출하여 답을 구성
"""
import sys


def solve(n, m, arr, flags):
    string = ""
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string
    for i in range(len(sorted_arr)):
        if not flags[i]:
            flags[i] = True
            arr.append(sorted_arr[i])
            string += solve(n, m, arr, flags)
            arr.pop()
            flags[i] = False
    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(unsorted_arr)
flags = [False for _ in range(len(sorted_arr))]
arr = []
answer = solve(n, m, arr, flags)
sys.stdout.write(answer[:-1])