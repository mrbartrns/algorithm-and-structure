# 단속카메라
"""
차량의 갯수는 1대이상 10000대 이하
[고속도로에 진입한 시점, 고속도로에 나간 시점]
start end가 없으면 cnt += 1

"""


def solution(routes):
    answer = 0
    return answer


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
routes.sort(key=lambda x: x[1] - x[0])
print(routes)