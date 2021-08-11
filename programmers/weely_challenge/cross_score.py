# 상호 평가
INF = 987654321


def solution(scores):
    answer = []
    for j in range(len(scores)):
        min_value = INF
        max_value = 0
        min_check = False
        max_check = False

        for i in range(len(scores)):
            if scores[i][j] >= max_value:
                if i == j and scores[i][j] > max_value:
                    max_check = True
                else:
                    max_check = False
                max_value = scores[i][j]
            if scores[i][j] <= min_value:
                if i == j and scores[i][j] < min_value:
                    min_check = True
                else:
                    min_check = False
                min_value = scores[i][j]

        s = 0
        cnt = 0
        for i in range(len(scores)):
            if i == j and (min_check or max_check):
                continue
            s += scores[i][j]
            cnt += 1

        ave = s / cnt
        if ave >= 90:
            answer.append("A")
        elif 80 <= ave < 90:
            answer.append("B")
        elif 70 <= ave < 80:
            answer.append("C")
        elif 50 <= ave < 70:
            answer.append("D")
        else:
            answer.append("F")
    return "".join(answer)


scores = [[70, 49, 90], [68, 50, 38], [73, 31, 100]]
print(solution(scores))
