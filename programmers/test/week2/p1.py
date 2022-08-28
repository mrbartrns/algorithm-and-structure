
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer

absolutes = [1, 2, 3]
signs = [False, False, True]
print(solution(absolutes, signs))