def divide(arr, idx_arr):
    if len(arr) == 1 and len(idx_arr) == 1:
        return [arr, idx_arr]
    else:
        i = 0
        j = len(arr)
        if len(arr) % 2 == 0:
            mid = (i + j) // 2
        else:
            mid = ((i + j) // 2) + 1
        left = divide(arr[:mid], idx_arr[:mid])
        right = divide(arr[mid:], idx_arr[mid:])
        
        return match(left, right) # left, right는 2차원 array로 구성

def match(left, right): # left, right[0] == arr, left, right[1] == idx_arr
    if left[0][0] == 1 and right[0][0] == 3:
        print('승자:', left[1][0])
        return left
    elif left[0][0] == 3 and right[0][0] == 1:
        print('승자:', right[1][0])
        return right
    elif left[0][0] == 2 and right[0][0] == 1:
        print('승자:', left[1][0])
        return left
    elif left[0][0] == 1 and right[0][0] == 2:
        print('승자:', right[1][0])
        return right
    elif left[0][0] == 3 and right[0][0] == 2:
        print('승자:', left[1][0])
        return left
    elif left[0][0] == 2 and right[0][0] == 3:
        print('승자:', right[1][0])
        return right
    elif left[0][0] == right[0][0]:
        print('승자:', left[1][0])
        return left

arr = [1, 1, 1, 1, 1, 1, 1]
idx_arr = [1, 2, 3, 4, 5, 6, 7]
# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     idx_arr = [i for i in range(1, len(arr) + 1)]
#     res = divide(arr, idx_arr)
#     print(f'#{i + 1} {res[1][0]}')
res = divide(arr, idx_arr)
print(res)