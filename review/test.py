arr = [1, 2, 3, 4, 5]
res = []
for i in range(len(arr)):
    s = 0
    for j in range(len(arr)):
        s += arr[(i + j) % len(arr)]
        res.append(s)
print(res)