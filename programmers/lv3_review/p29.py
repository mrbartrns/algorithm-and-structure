# 단속카메라
"""
시작지점과 끝지점을 모두 따로 저장하기
현재의 endpoint와 startpoint 비교
"""


def solution(routes):
    routes.sort(key=lambda x: x[0])
    end = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        if routes[i][0] > end:
            end = routes[i][1]
            answer += 1
        elif routes[i][1] <= end:
            end = routes[i][1]
    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
