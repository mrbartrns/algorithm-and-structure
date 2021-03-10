# SWEA 2029
t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    a1 = a // b
    a2 = a % b
    print("#" + str(tc + 1), a1, a2)
