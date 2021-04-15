# 부분집합 구하기
# def get_subset_bitlist():
#     bit = [0, 0, 0, 0]
#     for y in range(2):
#         bit[0] = y
#         for x in range(2):
#             bit[1] = x
#             for k in range(2):
#                 bit[2] = k
#                 for l in range(2):
#                     bit[3] = l
#                     print(bit)


arr = [3, 6, 7, 1, 5, 4]
# arr = [3, 6]
n = len(arr)

for i in range(1 << n):
    res = []
    for j in range(n):
        if i & (1 << j):
            res.append(arr[j])
    print(res)
