# 세그먼트 트리 구현하기
n = 12
arr = [5, 8, 7, 3, 2, 5, 1, 8, 9, 8, 7, 3]  # 기존의 배열을 트리라고 간주한 후 합 트리를 만든다.
tree = [0] * (n * 4)

# 세그먼트 트리 초기화
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]


# 구간 합을 구하는 함수
# 트리 구조를 가지고 있기 때문에 데이터를 탐색함에 있어 들이는 비용은 O(log(n))
# start: 시작 인덱스, end: 끝 인덱스 > 배열
# left, right = 구간 합을 구하고자 하는 범위
# 구간의 합은 범위 안에 있는 경우에 한해서만 더해주면 된다.
def get_sum(
    start: int, end: int, node: int, left: int, right: int
):  # node는 트리의 레벨과 같음. 처음에 1로 시작
    if left > end or right < start:
        return 0
    if left <= start and end <= right:  # 이게 무슨 뜻인지 잘 알기
        return tree[node]
    mid = (start + end) // 2
    val = get_sum(start, mid, node * 2, left, right) + get_sum(
        mid + 1, end, node * 2 + 1, left, right
    )
    return val


init(0, n - 1, 1)
print(tree)
print(get_sum(0, n - 1, 1, 3, 8))