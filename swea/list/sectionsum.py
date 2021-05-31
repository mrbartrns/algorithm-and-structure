def sum_section(arr, m):
    min_val = 0
    max_val = 0
    for i in range(len(arr) - m + 1):
        sum_val = 0
        for j in range(m):
            sum_val += arr[i + j]
        if min_val == 0 or min_val > sum_val:
            min_val = sum_val
        if max_val < sum_val:
            max_val = sum_val
    return max_val - min_val

# print(sum_section([3266, 9419, 3087, 9001, 9321, 1341, 7379, 6236, 5795, 8910, 2990, 2152, 2249, 4059, 1394, 6871, 4911, 3648, 1969, 2176], 19))
t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  print(f'#{i + 1} {sum_section(arr, m)}')