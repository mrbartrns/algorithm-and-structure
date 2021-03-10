idx = 0
a, b, c = map(int, input().split())
for i in range(a):
    for j in range(b):
        for k in range(c):
            idx += 1
            print(i, j, k)
print(idx)