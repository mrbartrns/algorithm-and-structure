# BOJ 6603번
"""
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 
첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다. 
"""
import sys


def solve(arr):
    """
    input: list, 기존 배열로부터 요소를 넣는 배열
    return: str
    """
    string = ""

    # 기저 사례
    if len(arr) == 6:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string

    for i in range(len(sets)):
        if not chosen[i]:
            chosen[i] = True
            if not arr or arr[-1] < sets[i]:
                arr.append(sets[i])
                string += solve(arr)
                arr.pop()
            chosen[i] = False
    return string


counter = 0

while True:
    a, *sets = list(map(int, sys.stdin.readline().split()))
    if a == 0:
        break
    if counter > 0:
        print("\n")
    arr = []
    chosen = [False] * len(sets)
    sys.stdout.write(solve(arr)[:-1])
    counter += 1