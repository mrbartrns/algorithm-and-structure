# 지형 편집
def solution(land, p, q):
    """

    Args:
        land(list): blocks(2D)
        p: 블록을 추가하는데 필요한 비용
        q: 블록을 제거하는데 필요한 비용

    Returns:

    """
    blocks = []
    for i in land:
        blocks += i

    blocks.sort()

    n = len(blocks)
    cost = (sum(blocks) - blocks[0] * n) * q
    answer = cost

    for i in range(1, n):
        if blocks[i] == blocks[i - 1]:
            continue

        cost += (p * i * (blocks[i] - blocks[i - 1])) - (q * (n - i) * (blocks[i] - blocks[i - 1]))
        answer = min(answer, cost)

    return answer


if __name__ == '__main__':
    land = [[4, 4, 3], [3, 2, 2], [2, 1, 0]]
    p = 5
    q = 3
    print(solution(land, p, q))
