# 이중 우선순위 큐
# 만약 힙을 이용한다면 어떻게 최댓값과 최소값을 구별할 수 있을것인지?
# 모두 삽입 후 최종적으로 두 힙의 교집합을 비교
import heapq as hq


def solution(operations):
    answer = [0, 0]
    minh = []
    maxh = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            hq.heappush(minh, int(operations[i][2:]))
            hq.heappush(maxh, -int(operations[i][2:]))
        elif operations[i][0] == "D" and operations[i][2:] == "1":
            if maxh:
                hq.heappop(maxh)
        else:
            if minh:
                hq.heappop(minh)
    maxh = list(map(lambda x: -x, maxh))
    min_set = set(minh)
    max_set = set(maxh)
    intersection = min_set & max_set
    ins = list(intersection)
    if len(ins) >= 2:
        ins.sort()
        answer = [ins[-1], ins[0]]
    return answer


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))