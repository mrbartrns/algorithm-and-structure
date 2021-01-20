# BOJ 1699번
import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n + 1):
        if i ** 0.5 - int(i ** 0.5) == 0:
            memo[i] = 1
        else:
            for j in range(1, int(i ** 0.5) + 1):
                if memo[i] > memo[i - j ** 2] + 1:
                    memo[i] = memo[i - j ** 2] + 1
    # print(memo)
    return memo[n]


n = int(input())
memo = [100001] * (n + 1)
sys.stdout.write(str(solve(n)))

"""
import sys

n = int(sys.stdin.readline())

arr = [i+1 for i in range(n)]

for i in range(1, n):
    sqr = (i+1)**(1/2)
    if int(sqr) == sqr :
        arr[i]=1
    else :
        for j in range(1, int(sqr)+1) :
            if arr[i]>arr[i-j*j]+1 :
                arr[i] = arr[i-j*j]+1
            
print(arr[n-1])
"""
