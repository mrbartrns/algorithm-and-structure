def func(a, n):
    if n == 1:
        return a
    else:
        if n % 2 == 0:
            return func(a, n // 2) * func(a, n // 2)
        else:
            return func(a, n - 1) * a


def solve1(n):
    if n < 10:
        print(n)
    else:
        solve1(n // 10)
        print(n % 10)

def solve2(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[-1] > solve2(arr[:len(arr) - 1]):
            return arr[-1]
        else:
            return solve2(arr[:len(arr) - 1])

def solve3(string):
    if len(string) == 1:
        return int(string)
    else:
        return 10 ** (len(string) - 1) * solve3(string[0]) + solve3(string[1:])

def solve4(arr):
    if len(arr) == 0:
        return 0
    else:
        if type(arr[-1]) == int:
            return arr[-1] +solve4(arr[:-1])
        else:
            return solve4(arr[-1]) + solve4(arr[: -1])

# print(solve4([1, 2, [3, 4], [5, 6]]))

def solve5(n):
    if n <= 0:
        return 0
    else:
        return n + solve5(n- 2)

# print(solve5(10))

def f1(n):
    if n == 1:
        return '*'
    else:
        return '*' * n + '\n' + f1(n - 1)

# print(f1(5))

def f2(n):
    if n == 1:
        print('*')
    else:
        f2(n - 1)
        print('*' * n)

f2(5)