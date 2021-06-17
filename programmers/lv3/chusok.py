# 추석 트래픽
"""
총길이가 3000인 배열을 만들고 그 안에서 조작하는 방법은 어떨지?
첫 배열의 값을 총 길이가 3000인 배열에 표시하기 -> 시작점을 0000 끝점을 3000
배열의 두번째 값을 표시하기 위해 배열의 두번째 값의 시작점과 끝점을 확인하기
기본적인 구조는 현재 구조와 비슷한 다이나믹 형식으로 가져가기
"""
MAX = 86400000


def solution(lines):
    start_t = []
    end_t = []
    for string in lines:
        info = string.split(" ")
        time = info[1]
        process_time = info[2]
        end_time = get_time(time)
        start_time = get_start_time(time, process_time)
        start_t.append(start_time)
        end_t.append(end_time)

    answer = 0
    for i in range(len(lines)):
        end_time = end_t[i] + 1000
        cnt = 0
        for j in range(i, len(lines)):
            if start_t[j] < end_time:
                cnt += 1
        answer = max(answer, cnt)

    return answer


def get_time(time):
    hour = int(time[:2])
    minute = int(time[3:5])
    second = int(time[6:8])
    millisecond = int(time[9:12])
    return (hour * 3600 + minute * 60 + second) * 1000 + millisecond


def get_start_time(time: str, processing_time):
    process = int(float(processing_time[:-1]) * 1000)
    return get_time(time) - process + 1


# 뭘 하는지 모를때에는 문자열 먼저 정리하기
if __name__ == "__main__":
    logs = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    print(solution(logs))
