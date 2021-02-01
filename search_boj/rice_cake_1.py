n = 4
m = 6
rice_cakes = [19, 15, 10, 17]
start = 0
end = max(rice_cakes)


def solve(start, end, target):
    res = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in range(len(rice_cakes)):
            if rice_cakes[i] > mid:
                total += rice_cakes[i] - mid
        if total < target:
            end = mid - 1

        else:
            res = mid
            start = mid + 1
    return res


print(solve(start, end, m))