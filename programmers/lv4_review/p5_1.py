# [카카오] 가사 검색
from bisect import bisect_left, bisect_right


def solution(words, queries):
    ret = []
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
            ret.append(get_count(r_board[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
        else:
            ret.append(get_count(board[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
    return ret


# 단어가 항상 좌, 우쪽으로 연결된 물음표가 존재하기 때문에 양쪽으로 이분탐색을 이용하여 문제 해결이 가능하다. -> 가운데 물음표 해결불가
def get_count(arr, left_value, right_value):
    left = bisect_left(arr, left_value)
    right = bisect_right(arr, right_value)
    return right - left


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
