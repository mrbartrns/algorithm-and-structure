# SWEA 2070
t = int(input())


def relation(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return 2


op = [">", "=", "<"]


for tc in range(t):
    a, b = map(int, input().split())
    s = relation(a, b)
    ans = op[s]
    print("#" + str(tc + 1), str(ans))