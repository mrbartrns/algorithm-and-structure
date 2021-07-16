# [카카오] 가사 검색
def solution(words, queries):
    answer = []
    for i in range(len(queries)):
        cnt = 0
        for j in range(len(words)):
            if len(queries[i]) != len(words[j]):
                continue

            left = search_left(queries[i])
            chk = True
            print(left)
            if left > 0:
                for k in range(left):
                    if queries[i][k] != words[j][k]:
                        chk = False
                        break
            else:
                right = search_right(queries[i])
                print(right)
                for k in range(right + 1, len(words[j])):
                    if queries[i][k] != words[j][k]:
                        chk = False
                        break
            if chk:
                cnt += 1
        answer.append(cnt)
    return answer


# 오른쪽에 ? 있을 때 오른쪽 끝 인덱스 반환
def search_left(query):
    start = 0
    end = len(query) - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if query[mid] == '?':
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


# 왼쪽에 ? 있을 때 오른쪽 끝 인덱스 반환
def search_right(query):
    start = 0
    end = len(query) - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if query[mid] == "?":
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "?????", "fr???", "fro???", "pro?"]
    # words = ['ab']
    # queries = ['??', '?a']
    print(solution(words, queries))
