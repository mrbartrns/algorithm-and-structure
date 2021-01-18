# BOJ 10974번
import sys


def solve(n, arr):
    answer = ""
    if len(arr) == n:
        for i in range(len(arr)):
            answer += str(arr[i])
            if i < len(arr) - 1:
                answer += " "
        answer += "\n"
        return answer

    for i in range(1, n + 1):
        if not flag[i]:
            flag[i] = True
            arr.append(i)
            answer += solve(n, arr)
            arr.pop()
            flag[i] = False
    return answer


n = int(sys.stdin.readline())
arr = []
flag = [False] * (n + 1)
answer = solve(n, arr)
sys.stdout.write(answer[:-1])