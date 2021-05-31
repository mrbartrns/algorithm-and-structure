N = int(input())
A = list(map(int, input().split()))

A.sort()
sumD = 0

numMax = A[-1]
numMin = A[0]
count = 0

while count < N - 1:
    numMax = A.pop()
    sumD += numMax - numMin
    count += 1
    numMin = A.pop(0)
    if len(A) == 1:
        if numMax - A[0] > A[0] - numMin:
            sumD += numMax - A[0]
        else:
            sumD += A[0] - numMin
        count += 1
    elif len(A) == 0:
        break
    else:
        sumD += numMax - A[0]
        count += 1

print(sumD)