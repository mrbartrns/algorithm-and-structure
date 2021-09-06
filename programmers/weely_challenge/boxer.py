# 복서 정렬하기
import heapq


def solution(weights, head2head):
    answer = []
    q = []
    for i in range(len(weights)):
        cnt = 0
        win_cnt = 0
        win_weight_cnt = 0
        for j in range(len(weights)):
            if head2head[i][j] == 'N':
                continue
            cnt += 1
            if head2head[i][j] != 'W':
                continue
            win_cnt += 1
            if weights[i] < weights[j]:
                win_weight_cnt += 1
        value = 0 if cnt == 0 else win_cnt / cnt
        heapq.heappush(q, (-value, -win_weight_cnt, -weights[i], i + 1))
    while q:
        answer.append(q[0][3])
        heapq.heappop(q)

    return answer


if __name__ == '__main__':
    weights = [50, 82, 75, 120]
    head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
    print(solution(weights, head2head))
