# 지형 편집
def solution(land, p, q):
    blocks = []
    total = 0
    for i in range(len(land)):
        for j in range(len(land)):
            blocks.append(land[i][j])
            total += land[i][j]
    blocks.sort()
    s = (total - blocks[0] * len(blocks)) * q
    cost = s
    for i in range(1, len(blocks)):
        up = (blocks[i] - blocks[i - 1]) * i * p
        down = (blocks[i] - blocks[i - 1]) * (len(blocks) - i) * q
        s += up - down
        cost = min(s, cost)
    return cost


if __name__ == '__main__':
    land = [[1, 2], [2, 3]]
    p = 3
    q = 2
    print(solution(land, p, q))
