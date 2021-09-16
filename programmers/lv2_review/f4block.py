# [카카오] 프렌즈4블록
def scroll_down(game_board):
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if game_board[y][x] == "":
                for k in range(y, 0, -1):
                    game_board[k][x] = game_board[k - 1][x]
                game_board[0][x] = ""


def erase_and_add_count(visited, game_board):
    cnt = 0
    for y in range(len(visited)):
        for x in range(len(visited[0])):
            if visited[y][x]:
                cnt += 1
                game_board[y][x] = ""
    return cnt


def make_game_board(m, n, board):
    game_board = []
    for i in range(m):
        game_board.append(list(board[i]))
    return game_board


def solution(m, n, board):
    """main function

    Args:
        m (int): row
        n (int): col
        board (list): game board
    """
    game_board = make_game_board(m, n, board)
    answer = 0
    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]
        done = True

        # insection
        for y in range(m - 1):
            for x in range(n - 1):
                if game_board[y][x] != "" and (
                    game_board[y][x]
                    == game_board[y][x + 1]
                    == game_board[y + 1][x]
                    == game_board[y + 1][x + 1]
                ):
                    done = False
                    (
                        visited[y][x],
                        visited[y][x + 1],
                        visited[y + 1][x],
                        visited[y + 1][x + 1],
                    ) = (True, True, True, True)
        if done:
            break

        # erase
        answer += erase_and_add_count(visited, game_board)

        # scroll down
        scroll_down(game_board)
    return answer


if __name__ == "__main__":
    m = 6
    n = 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print(solution(m, n, board))