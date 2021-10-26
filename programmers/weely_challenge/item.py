# 11주차 아이템 줍기
# TODO: 완벽하게 1의 모양이 나오도록 고치기
def draw_graph(graph, x1, y1, x2, y2):
    bx1, bx2 = x1, x2
    by1, by2 = y1, y2
    if bx2 < bx1:
        bx1, bx2 = bx2, bx1
    if by2 < by1:
        by1, by2 = by2, by1
    for i in range(bx1, bx2 + 1):
        graph[by2][i] += 1
    for i in range(by1, by2 + 1):
        graph[i][bx2] += 1
    for i in range(bx2 + 1, bx1, -1):
        graph[by1][i] += 1
    for i in range(by2 + 1, by1, -1):
        graph[i][bx1] += 1


def solution(rectangle, character_x, character_y, item_x, item_y):
    answer = 0
    graph = [[0 for _ in range(10)] for _ in range(10)]
    for x1, y1, x2, y2 in rectangle:
        draw_graph(graph, x1, y1, x2, y2)
        break
    for i in range(10):
        for j in range(10):
            print(graph[i][j], end=" ")
        print()
    return answer


if __name__ == "__main__":
    print(
        solution(
            rectangle=[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]],
            character_x=1,
            character_y=3,
            item_x=7,
            item_y=8,
        )
    )
