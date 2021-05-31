# BOJ 1181
n = int(input())
arr = []
check = {}
for _ in range(n):
    c = input()
    arr.append(c)
    check[c] = False

arr.sort(key=lambda x: (len(x), x))
for i in range(len(arr)):
    if not check[arr[i]]:
        print(arr[i])
        check[arr[i]] = True