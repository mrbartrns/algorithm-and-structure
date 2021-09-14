# [카카오] 문자열 압축
INF = 987654321


def solution(s):
    if len(s) <= 1:
        return 1
    answer = INF
    for cnt in range(1, len(s) // 2 + 1):
        string = ""
        piece = ""
        count = 1
        for i in range(0, len(s), cnt):
            j = i + cnt
            print(s[i:j])
            if s[i:j] != piece:
                string += str(count) + piece if count > 1 else piece
                piece = s[i:j]
                count = 1
            else:
                count += 1
        string += str(count) + piece if count > 1 else piece
        print(string)
        answer = min(answer, len(string))
    return answer


if __name__ == "__main__":
    s = "aaa"
    print(solution(s))
