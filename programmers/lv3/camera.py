# 단속 카메라
def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])
    out = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > out:
            out = routes[i][1]
            answer += 1
        elif routes[i][1] <= out:
            out = routes[i][1]
    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
