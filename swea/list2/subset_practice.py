

def get_count(n, k):
    counts = 0
    arr = [i for i in range(1, 13)]
    length = len(arr)
    for i in range(1 << length):
        res = []
        for j in range(length):
            if i & (1 << j):
                res.append(arr[j])
        if len(res) == n and sum(res, start=0) == k:
            counts += 1
    return counts

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    counts = get_count(n, k)
    print(f'#{i + 1} {counts}')
# print(get_count(5, 15))
