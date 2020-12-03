def f(n):
    if n <= 1:
        return 1
    else:
        if n % 2 == 0:
            return 2 * f(n - 1) + 1
        else:
            return 2 * f(n - 1) - 1

def dp(n):
    m = [0, 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            m.append(2 * m[i - 1] + 1)
        else:
            m.append(2 * m[i - 1] - 1)
    return m[n]

t = int(input())
for i in range(t):
    n = int(input())
    print(f'#{i + 1} {dp(n // 10)}')