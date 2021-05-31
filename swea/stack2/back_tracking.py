def back_tracking(arr, issued, n, m, k):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
    else:
        
        for i in range(1, n + 1):
            if not issued[i]:
                print(k)
                arr[k] = i
                print(arr)
                issued[i] = True
                back_tracking(arr, issued, n, m, k + 1)
                issued[i] = False

n = 4
m = 3
arr = [0] * m
issued = [False] * (n + 1)
k = 0
back_tracking(arr, issued, n, m, k)