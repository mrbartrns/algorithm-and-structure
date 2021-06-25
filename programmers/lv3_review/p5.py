# 디스크 컨트롤러
"""
현재 실행중인 작업이 없다면, 바로 작업을 실행
이미 실행중인 작업이 있다면, 작업을 큐에다가 삽입(실행시간이 짧은 순으로 정렬하기)
"""
import heapq


def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    idx = 0
    answer = 0
    time = 0
    q = []
    while idx < len(jobs) or q:
        while idx < len(jobs) and time >= jobs[idx][0]:
            req_time = jobs[idx][0]
            process_time = jobs[idx][1]
            heapq.heappush(q, (process_time, req_time))
            idx += 1

        if q:
            process_time, req_time = heapq.heappop(q)
            time += process_time
            answer += time - req_time
        else:
            req_time, _ = jobs[idx]
            time = req_time
    return answer // len(jobs)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
