"""
재귀함수를 사용하기 위해서는 자기 자신을 해결 후 어느 부분을 넘겨줄지 정해야 함
1. 어느 부분을 분할 할지
- 조건에 맞춰서 리스트에 요소를 추가 하는 것
2. 기저 사례
- 배열의 크기가 조건을 만족하면 스트링을 반환한다.
3. 어느 부분을 반복 할지 (자기 자신을 해결하기 위해서 어떤 조건을 넣어야 할 지? -> 자기 자신까지 완벽히 해결하기 위하여 분할후 반복시에 조건을 넣어야 한다.)
"""


import sys


def solve(n, m, arr):
    string = ""
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string
    for i in range(1, n + 1):
        arr.append(i)
        string += solve(n, m, arr)
        arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
arr = []
answer = (solve(n, m, arr))[:-1]
print(answer)