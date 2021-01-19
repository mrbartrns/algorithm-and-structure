# 백준 쉬운수
# 자릿수 배열을 만들고, 인덱스를 0과 9로 각 자릿수를 나타낸다.

arr = [[0 for _ in range(10)] for _ in range(100)]
for i in range(1, len(arr[0])):
    arr[0][i] = 1


def solve(n):
    for i in range(99):
        for j in range(10):
            if j >= 1:
                arr[i + 1][j - 1] += arr[i][j]
            if j < 9:
                arr[i + 1][j + 1] += arr[i][j]
    value = (sum(arr[n - 1])) % 1000000000
    return value