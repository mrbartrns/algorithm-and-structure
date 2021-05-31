def pizza(n):
    if n == 1:
        return 2
    else:
        return n + pizza(n - 1)

print(pizza(4))