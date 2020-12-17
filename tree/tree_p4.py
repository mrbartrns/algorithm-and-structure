# 완전한 이진트리 이므로 배열 사용
# arr = [None, 0, 0, 3, 1, 2]
# arr = [None, 0, 0, 0, 0, 0, 501, 170, 42, 468, 335]
arr = [None, 0, 0, 0, 0, 0, 0, 0, 0, 963, 465, 706, 146, 282, 828, 962, 479, 359]

# 2번 노드의 값을 알고 싶음
def get_sum(arr, idx):
    if idx < len(arr):
        if arr[idx] == 0:
            value = 0
            if idx * 2 < len(arr):
                value += get_sum(arr, idx * 2)
            if idx * 2 + 1 < len(arr):
                value += get_sum(arr, idx * 2 + 1)
            arr[idx] = value
            return value
        else:
            return arr[idx]


t = int(input())
for tc in range(t):
    nodes, leafs, res = map(int, input().split())
    arr = [0] * (nodes + 1)
    arr[0] = None
    for _ in range(leafs):
        index, value = map(int, input().split())
        arr[index] = value
    print(f"#{tc + 1} {get_sum(arr, res)}")

# print(get_sum(arr, 4))