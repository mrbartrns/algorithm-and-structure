def get_min_max(arr):
  min_val = 0
  max_val = 0
  for i in range(len(arr)):
    if min_val > arr[i] or min_val == 0:
      min_val = arr[i]
    if max_val < arr[i]:
      max_val = arr[i]
    
  return max_val - min_val


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  print(f'#{i + 1} {get_min_max(arr)}')

