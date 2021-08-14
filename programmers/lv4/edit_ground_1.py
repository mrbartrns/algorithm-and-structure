# 지형 편집
"""
https://programmers.co.kr/learn/courses/30/lessons/12984
가장 비용이 적은 층에 맞추려고 할 때 비용 찾기
* 처음에 접근하려고 했던 방식 -> bisection search 그러나 양 끝점이 모두 최솟값이 아니므로
* 이차함수의 꼴을 가지며, 최솟값을 찾기 위해서는 이분탐색이 아닌 삼분탐색으로 접근해야 한다.
* 또한 시간상으로 이득을 볼게 없다.

> 해결 방안: 한 칸씩 분석하는것이 아닌, 한 층씩 분석하는 방법을 사용하기 (greedy algorithms)
1. 한 칸씩이 아닌 한 층씩 분석하기 위해서는 정렬 필요
2. 처음 blocks[0]에 값을 맞출때 총 cost는 total - (blocks[0]) * len(blocks)(총 blocks의 갯수만큼 blocks[0] 층을 가지고 있다)
3. 여기서 한층씩 더해나가면서 올리는데 필요한 비용을 더하고, 내리는데 필요한 비용을 빼기
4. 이때 변화하는 층은 blocks[i] - blocks[i - 1]만큼의 층수가 변화하고, 이는 내리는데 필요한 비용에서도 마찬가지 이다.
"""


def solution(land, p, q):
    blocks = []
    total = 0
    for i in range(len(land)):
        for j in range(len(land)):
            blocks.append(land[i][j])
            total += land[i][j]
    blocks.sort()

    cost = (total - blocks[0] * (len(blocks))) * q
    answer = cost
    for i in range(1, len(blocks)):
        # 0에서부터 i까지의 거리
        up = i * (blocks[i] - blocks[i - 1]) * p
        # len(blocks)에서부터 i까지 거리만큼 내려주는 값이 변화했다.
        down = (len(blocks) - i) * (blocks[i] - blocks[i - 1]) * q
        cost += up - down
        answer = min(answer, cost)
    return answer


if __name__ == '__main__':
    land = [[4, 4, 3], [3, 2, 2], [2, 1, 0]]
    p = 5
    q = 3
    print(solution(land, p, q))
