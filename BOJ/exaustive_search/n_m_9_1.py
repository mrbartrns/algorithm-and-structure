import sys


def solve(flags, arr):
    string = ""
    double = -1

    if len(arr) == m:
        for i in range(len(arr)):
            string += str(arr[i])
            if i < len(arr) - 1:
                string += " "
        string += "\n"
        return string

    # 지금 이 부분 원리 파악하고 복습하기
    # 이해하기 쉽기 위해 스택과 상관없이 같은 수를 만났을때 어떻게 대처했는지 생각해보기
    # 다음 스택으로 넘어갔을때 상태 변화가 어떠한지 -> flag같은경우는 이전과 이어지므로 전역변수, stack
    for i in range(len(numbers)):
        if not flags[i] and (double != numbers[i]):
            flags[i] = True
            double = numbers[i]
            arr.append(numbers[i])
            string += solve(flags, arr)
            arr.pop()
            flags[i] = False

    return string


n, m = map(int, sys.stdin.readline().split())
unsorted_arr = list(map(int, sys.stdin.readline().split()))
numbers = sorted(unsorted_arr)
arr = []
flags = [False for _ in range(len(numbers))]
visited = []
answer = solve(flags, arr)
sys.stdout.write(answer[:-1])