# [카카오] 무지의 먹방 라이브
# 그리디 알고리즘 -> 단순한 것부터 시작 후 시간복잡도 줄여나가기
# 계속 순환 반복하는 구조를 줄여나가는 방법은 어떤지?
def solution(food_times, k):
    idx = 0
    cnt = 0
    while cnt < k:
        if food_times[idx] > 0:
            food_times[idx] -= 1
            cnt += 1
        idx = (idx + 1) % len(food_times)
    # 아무것도 먹을 것이 없을 때에 -1을 반환하기
    current = idx
    while food_times[idx] == 0:
        idx = (idx + 1) % len(food_times)
        if idx == current:
            return -1
    return idx + 1


if __name__ == "__main__":
    food_times = [7, 8, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]
    k = 35
    print(solution(food_times, k))
