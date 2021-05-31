def special_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i + 1, len(arr)):
            if i % 2 == 0:
                if arr[idx] < arr[j]:
                    idx = j
            else:
                if arr[idx] > arr[j]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
        
    return arr

t = int(input())
for i in range(t):
    string = ''
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = special_sort(arr)
    k = len(new_arr) if len(new_arr) <= 10 else 10
    for j in range(k):
        string += str(new_arr[j])
        string += ' '
    print(f'#{i + 1} {string}')

# print(special_sort([3, 69, 21, 46, 43, 60, 62, 97, 64, 30, 17, 88, 18, 98, 71, 75, 59, 36, 9, 26]))