from bisect import bisect_left, bisect_right


def solution(words, queries):
    board = [[] for _ in range(10001)]
    board_rev = [[] for _ in range(10001)]
    answer = []

    for word in words:
        board[len(word)].append(word)
        board_rev[len(word)].append(word[::-1])
    for i in range(1, 10001):
        board[i].sort()
        board_rev[i].sort()

    for query in queries:
        if query[0] == "?":
            answer.append(
                get_counts(
                    board_rev[len(query)],
                    query[::-1].replace("?", "a"),
                    query[::-1].replace("?", "z"),
                )
            )
        else:
            answer.append(
                get_counts(
                    board[len(query)], query.replace("?", "a"), query.replace("?", "z")
                )
            )
    return answer


def get_counts(arr, left_value, right_value):
    left = bisect_left(arr, left_value)
    right = bisect_right(arr, right_value)
    return right - left


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))