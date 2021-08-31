# 지형 편집

def solution(land, p, q):
    blocks = []
    total = 0
    for i in range(len(land)):
        for j in range(len(land)):
            blocks.append(land[i][j])
            total += land[i][j]
    blocks.sort()
    # 깎는데 필요한 비용
    s = (total - blocks[0] * len(blocks)) * q
    cost = s
    for i in range(1, len(blocks)):
        up = (blocks[i] - blocks[i - 1]) * i * p
        down = (blocks[i] - blocks[i - 1]) * (len(blocks) - i) * q
        s += up - down
        cost = min(s, cost)
    return cost


if __name__ == '__main__':
    land = [[4, 4, 3], [3, 2, 2], [2, 1, 0]]
    p = 5
    q = 3
print(solution(land, p, q))
