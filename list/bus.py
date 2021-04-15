def bus(k, arr, last):
    s = 0
    r = 0
    m = 0
    if last - arr[-1] > k:
        return 0
    else:
        for i in range(len(arr) - 1):
            if arr[i] - s <= k:
                # do something
                r += (arr[i] - s)
                if r == k:
                    m += 1
                    r = 0
                else:
                    if r + arr[i + 1] - arr[i] > k:
                        m += 1
                        r = 0
                s = arr[i]
            else:
                return 0
        if arr[-1] - s <= k:
            r += arr[-1] - s
            if r == k:
                m += 1
                r = 0
                return m
            else:
                if r + last - arr[-1] > k:
                    m += 1
                    r = 0
                return m
        else:
            return 0

# t = int(input())
# for y in range(t):
#     k, last, n = map(int, input().split())
#     arr = list(map(int, input().split()))
#     print(f'#{y + 1} {bus(k, arr, last)}')

# print(bus(5, [4, 7, 9, 14, 17], 20))
# print(bus(3, [1, 3, 5, 7, 9], 10))
# print(bus(3, [1, 3, 7, 8, 9], 10))
print(bus(5, [5, 10, 15], 20))