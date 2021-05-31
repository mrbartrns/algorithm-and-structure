"""
1. 어느 부분을 분할 할 지
- 리스트에 요소를 추가하는 것
2. 기저 사례
- 배열의 크기가 m을 만족하면, 스트링을 반환
3. 어느 부분을 자기자신이 완벽히 해결하고 넘겨줄지
- 조건에 맞춰(비 내림차순) 리스트에 넣고 스트링을 반환받는다. 이때 지역변수로 n, m, arr를 저장한다.
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
        if not arr or arr[-1] <= i:
            arr.append(i)
            # 해결한 일부에 대해서 반환받은후 스택이 0이 될 때 까지 반환. 답의 일부를 만듬
            string += solve(n, m, arr)
            arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
arr = []
answer = (solve(n, m, arr))[:-1]
print(answer)