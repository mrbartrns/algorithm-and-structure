from bisect import bisect_left, bisect_right

arr = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
print(bisect_left(arr, 2))
print(bisect_right(arr, 2))
