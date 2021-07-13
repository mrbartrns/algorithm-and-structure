def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])
    last_time = routes[0][1]
    for i in range(1, len(routes)):
        if last_time < routes[i][0]:
            answer += 1
            last_time = routes[i][1]
        elif routes[i][1] < last_time:
            last_time = routes[i][1]
    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
