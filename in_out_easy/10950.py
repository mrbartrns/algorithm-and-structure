# BOJ 10950
def add(a, b):
    return a + b


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(add(a, b))