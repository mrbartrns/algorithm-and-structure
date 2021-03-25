# BOJ 2529
import sys


def backtrack(k, n, string):
    if k == n:
        numbers.append(string)
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            if not string:
                backtrack(k + 1, n, string + str(i))
            else:
                if sign[k - 1] == "<" and int(string[k - 1]) < i:
                    backtrack(k + 1, n, string + str(i))
                elif sign[k - 1] == ">" and int(string[k - 1]) > i:
                    backtrack(k + 1, n, string + str(i))
            visited[i] = False


si = sys.stdin.readline
n = int(si())
sign = list(si().split())
visited = [False] * 10
numbers = []
res = []
MAX = -1
MIN = 1e12
max_val = ""
min_val = ""

backtrack(0, n + 1, "")

for num_set in numbers:
    flag = True
    for i in range(n):
        if sign[i] == "<":
            if num_set[i] > num_set[i + 1]:
                flag = False
                break
        elif sign[i] == ">":
            if num_set[i] < num_set[i + 1]:
                flag = False
                break
    if flag:
        if int(num_set) > MAX:
            MAX = int(num_set)
            max_val = num_set
        if int(num_set) < MIN:
            MIN = int(num_set)
            min_val = num_set

print(max_val)
print(min_val)