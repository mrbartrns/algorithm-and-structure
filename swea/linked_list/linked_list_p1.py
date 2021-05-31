# 파이썬 함수를 이용한 숫자 추가

t = int(input())
for i in range(t):
    arr_len, add_counts, idx = map(int, input().split())
    arr = [int(x) for x in input().split()]
    for _ in range(add_counts):
        index, num = map(int, input().split())
        arr.insert(index, num)
    print(f"#{i + 1} {arr[idx]}")
