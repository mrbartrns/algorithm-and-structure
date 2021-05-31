def bisection_search(p, c): # left = 0, right = p
    counts = 0
    left = 1
    right = p
    mid = (left + right) // 2
    flag = True

    while flag:
        counts += 1
        if mid == c:
            return counts
        else:
            if mid < c:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2


t = int(input())
for i in range(t):
    res = ''
    p, pa, pb = map(int, input().split())
    counts_a = bisection_search(p, pa)
    counts_b = bisection_search(p, pb)
    if counts_a == counts_b:
        res = '0'
    elif counts_a < counts_b:
        res = 'A'
    elif counts_a > counts_b:
        res = 'B'
    print(f'#{i + 1} {res}')
        