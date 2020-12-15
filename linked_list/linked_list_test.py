def hello(n):
    if n == 1:
        return "hi"
    else:
        non = hello(n - 1)
        return non


print(hello(10))