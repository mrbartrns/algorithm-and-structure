# 위장


"""
def solution(clothes):
    def dfs_left(s, idx):
        if idx == half:
            left.append(s)
            return
        dfs_left(s, idx + 1)
        dfs_left(s * values[idx], idx + 1)

    def dfs_right(s, idx):
        if idx == len(values):
            right.append(s)
            return
        dfs_right(s, idx + 1)
        dfs_right(s * values[idx], idx + 1)

    clothes_dic = {}
    for _, v in clothes:
        clothes_dic[v] = clothes_dic.get(v, 0) + 1
    values = list(clothes_dic.values())
    half = len(values) // 2
    left, right = [], []
    dfs_left(1, 0)
    dfs_right(1, half)
    answer = sum(left) + sum(right) - 2
    for i in range(1, len(left)):
        s = 0
        for j in range(1, len(right)):
            s += left[i] * right[j]
        answer += s
    return answer



"""


def solution(clothes):
    categories = {}
    for _, c in clothes:
        if c not in categories:
            categories[c] = 2
        else:
            categories[c] += 1

    cnt = 1
    values = list(categories.values())
    for i in range(len(values)):
        cnt *= values[i]
    cnt -= 1
    return cnt


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
print(solution(clothes))