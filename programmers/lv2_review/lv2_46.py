# 프렌즈4블록


def solution(m, n, board):
    # board 가공
    board = list(map(lambda x: list(x), board))
    ans = 0
    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]
        changed = False
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != "" and (
                    board[i][j]
                    == board[i][j + 1]
                    == board[i + 1][j]
                    == board[i + 1][j + 1]
                ):
                    if not visited[i][j]:
                        visited[i][j] = True
                        ans += 1
                    if not visited[i][j + 1]:
                        visited[i][j + 1] = True
                        ans += 1
                    if not visited[i + 1][j]:
                        visited[i + 1][j] = True
                        ans += 1
                    if not visited[i + 1][j + 1]:
                        visited[i + 1][j + 1] = True
                        ans += 1

                    changed = True

        # 칸 갱신하기
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    board[i][j] = ""

        # 빈칸을 채우기
        if changed:
            for j in range(n):
                for i in range(m):
                    if board[i][j] == "":
                        for k in range(i):
                            board[i - k][j], board[i - 1 - k][j] = (
                                board[i - 1 - k][j],
                                board[i - k][j],
                            )
        else:
            return ans


m = 6
n = 6
# board = [
#     ["T", "T", "T", "A", "N", "T"],
#     ["R", "R", "F", "A", "C", "C"],
#     ["R", "R", "R", "F", "C", "C"],
#     ["T", "R", "R", "R", "A", "A"],
#     ["T", "T", "M", "M", "M", "F"],
#     ["T", "M", "M", "T", "T", "J"],
# ]
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))