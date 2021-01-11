"""
자연수 n과 m이 주어졌을 때, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램 작성하기
재귀 호출을 이용하기 위해서는 문제를 이루는 조각중 하나를 떼내어 자신이 해결하고, 나머지를 넘긴다.
단, 수열은 오름차순이어야 한다.
1. 어떤작업을 분할 할 것인가?
- 리스트에 요소를 조건에 맞게 하나씩 추가하기 > 추가시에 조건을 달지, 기저조건에 달지 확인
2. 기저 조건
- 수열이 조건을 만족하면 스트링으로 변환하여 반환한다.
3. 어떤 행위를 반복?
- 중복 및 오름차순으로 리스트에 요소를 추가
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
        if not arr or arr[-1] < i:
            arr.append(i)
            string += solve(n, m, arr)
            arr.pop()
    return string


n, m = map(int, sys.stdin.readline().split())
arr = []
answer = (solve(n, m, arr))[:-1]
print(answer)