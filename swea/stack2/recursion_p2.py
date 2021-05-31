def func(n):
    if n == 1:
        for i in range(2 ** 1):
            for j in range(2 ** 1):
                print(i, j)
    else:
        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                func(n - 1)
# func(3)

def rec(x, y):
    if y > x:
        x += 1
        y -= 1
        print(x, y)
        rec(x, y)
        print(x ,y)

def f1(string):
    if len(string) == 1:
        return string
    else:
        reversed_string = ''
        left = string[-1]
        right = f1(string[:-1])
        reversed_string += left
        reversed_string += right
        return reversed_string

def f2(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + f2(string[:-1])

print(f1('string'))