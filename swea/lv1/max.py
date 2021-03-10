# SWEA 2068
t = int(input())

for tc in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    print("#" + str(tc + 1), str(arr[-1]))