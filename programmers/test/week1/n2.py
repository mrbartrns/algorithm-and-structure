"""
모든 명함들이 들어갈 수 있게 지갑을 만든다. 따라서 지갑의 가로 * 세로는 
모든 명함을 커버할 수 있도록 각 명함의 가로와 세로의 최댓값을 가져야 한다.

명함은 회전할 수 있으므로 작은 것은 작은 것끼리, 큰 것은 큰 것끼리 모으면
편차가 적어진다. -> 편자가 작다는 말은 곧 최소를 만들 수 있다와 동일하다.
"""


def solution(sizes):
    # 최소가 항상 앞으로 오도록 정렬한다.
    new_sizes = list(map(lambda x: [x[1], x[0]] if x[0] > x[1] else x, sizes))
    min_width = sorted(new_sizes, key=lambda x: x[0])[-1][0]
    min_height = sorted(new_sizes, key=lambda x: x[1])[-1][1]
    return min_width * min_height


# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
