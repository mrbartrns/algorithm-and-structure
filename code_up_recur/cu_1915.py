import sys


def get_fibo(n, arr, k=0):
    if k == n + 1:
        return
    else:
        fibo = (arr[k - 1] + arr[k - 2]) % 10009
        arr.append(fibo)
        get_fibo(n, arr, k + 1)
        return fibo


n = int(sys.stdin.readline())

arr = [0, 1]
get_fibo(n, arr, 2)
print(arr[-1])