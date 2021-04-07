# 추석 트래픽
def solution(lines):
    answer = 0
    return answer


# 뭘 하는지 모를때에는 문자열 먼저 정리하기
string = "2016-09-15 01:00:04.001 2.0s"


def process(string):
    end = string[11:23]
    done = float(string[24:27])
    sec = float(end[6:])
    print(sec - done)


process(string)