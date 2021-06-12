# 디스크 컨트롤러
import heapq


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    q = []
    ret = []
    time = 0
    idx = 0
    while idx < len(jobs) or q:
        if idx < len(jobs) and time >= jobs[idx][0]:
            req_time = jobs[idx][0]
            process_time = jobs[idx][1]
            heapq.heappush(q, (process_time, req_time))
            idx += 1
            continue
        if q:
            process_time, req_time = heapq.heappop(q)
            time += process_time
            answer += time - req_time
        else:
            req_time, process_time = jobs[idx]
            time = req_time
    return answer // len(jobs)


if __name__ == "__main__":
    jobs = [[0, 3], [4, 4], [5, 3], [4, 1]]
    print(solution(jobs))
