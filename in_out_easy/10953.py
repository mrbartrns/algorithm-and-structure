def add(a, b):
    return a + b


n = int(input())
for _ in range(n):
    a, b = map(int, input().split(","))
    print(add(a, b))