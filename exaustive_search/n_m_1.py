"""
자연수 n과 m이 주어졌을 때, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램을 작성하기
재귀 호출을 이용하기 위해서는, 조각들 중 하나를 떼내어 자신이 해결하고 나머지를 미래의 나에게 넘겨줌
1. 먼저 어떤 작업을 분할 할 것인가?
- 어떤 것을 추가하는 행위를 반복한다.
2. 언제 끝낼 것인가? 기저 조건
- 어떤 것을 받았을 때, 길이가 주어진 조건을 만족하면 리스트 내의 요소들을 한줄로 출력
3. 어떤 행위를 반복할 것인가?
- 중복 없이 리스트에 요소를 추가.
"""
import sys


def solve(n, m, arr, flags):
    string = ""
    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i != len(arr) - 1:
                string += " "
        string += "\n"
        return string
    for i in range(1, n + 1):
        if not flags[i]:
            flags[i] = True
            arr.append(i)
            string += solve(n, m, arr, flags)
            arr.pop()
            flags[i] = False
    return string


n, m = map(int, sys.stdin.readline().split())
arr = []
flags = [False] * (n + 1)
answer = solve(n, m, arr, flags)
sys.stdout.write(answer[:-1])