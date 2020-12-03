def get_minimum_sum(arr: list, issued: list, sum_list: list, min_val: list, k: int):
    if k == len(arr):
        counts = 0
        for i in range(len(sum_list)):
            counts += sum_list[i]
        if min_val[0] == 0 or min_val[0] > counts:
            min_val[0] = counts
        sum_list = []
        return
    else:
        for i in range(len(arr[k])):
            if not issued[i]: # issued는 열 검사
                issued[i] = True
                sum_list.append(arr[k][i]) # 더하기
                if min_val[0] == 0 or sum(sum_list) <= min_val[0]:
                    get_minimum_sum(arr, issued, sum_list, min_val, k + 1)
                sum_list.pop()
                issued[i] = False

# t = int(input())
# for i in range(t):
#     min_val = [0]
#     n = int(input())
#     arr = []
#     sum_list = []
#     for _ in range(n):
#         temp = [int(x) for x in input().split()]
#         arr.append(temp)
    
#     issued = [False] * len(temp)
#     get_minimum_sum(arr, issued, sum_list, min_val, 0)


#     print(f'#{i + 1} {min_val[0]}')




min_val = [0]
sum_list = []
issued = [False] * 50 # Todo: True False를 count로 바꾼다.
arr = [
    [9, 4, 7],
    [8, 6, 5],
    [5, 3, 7]
] # [4, 5, 3]
# arr = [
#     [1 for _ in range(50)]
# ] * 50

get_minimum_sum(arr, issued, sum_list, min_val, 0)
print(min_val)