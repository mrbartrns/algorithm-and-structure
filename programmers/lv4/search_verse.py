# [카카오] 가사 검색

from bisect import bisect_left, bisect_right


def get_count(arr, left_value, right_value):
    left = bisect_left(arr, left_value)
    right = bisect_right(arr, right_value)
    return right - left


def solution(words, queries):
    answer = []
    board = [[] for _ in range(10001)]
    r_board = [[] for _ in range(10001)]
    for word in words:
        board[len(word)].append(word)
        r_board[len(word)].append(word[::-1])
    for i in range(len(board)):
        board[i].sort()
        r_board[i].sort()

    for query in queries:
        if query[0] == "?":
            answer.append(
                get_count(
                    r_board[len(query)],
                    query[::-1].replace("?", "a"),
                    query[::-1].replace("?", "z"),
                )
            )
        else:
            answer.append(
                get_count(
                    board[len(query)], query.replace("?", "a"), query.replace("?", "z")
                )
            )
    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))