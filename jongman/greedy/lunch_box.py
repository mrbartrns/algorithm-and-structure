import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    n = int(si())
    cooking_time = list(map(int, si().split()))
    eating_time = list(map(int, si().split()))
    arr = [(cooking_time[i], eating_time[i]) for i in range(n)]
    arr.sort(key=lambda x: -x[1])
    time = 0
    answer = 0
    for i in range(n):
        time += arr[i][0]
        answer = max(time + arr[i][1], answer)
    print(answer)
