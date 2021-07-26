# [카카오] 가사 검색
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    board = [[] for _ in range(10001)]
    reversed_board = [[] for _ in range(10001)]
    for word in words:
        board[len(word)].append(word)
        reversed_board[len(word)].append(word[::-1])  # 뒤집어서 삽입하기

    for i in range(10001):
        board[i].sort()
        reversed_board[i].sort()

    for query in queries:
        if query[0] == "?":
            ret = get_counts(
                reversed_board[len(query)],
                query[::-1].replace("?", "a"),
                query[::-1].replace("?", "z"),
            )
        else:
            ret = get_counts(
                board[len(query)], query.replace("?", "a"), query.replace("?", "z")
            )
        answer.append(ret)
    return answer


def get_counts(words, left_value, right_value):
    left = bisect_left(words, left_value)
    right = bisect_right(words, right_value)
    return right - left


# 뒤에 있을 때에는 a - z 전 범위가 되기 때문에 뒤집어서 해야 함


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))