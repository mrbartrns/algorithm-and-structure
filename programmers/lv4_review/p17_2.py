# 지형 편집
def solution(land, p, q):
    """문제에 대한 해답

    Args:
        land (list): 블록들의 개수가 담겨진 2차원 배열
        p (int): 블록 한 개를 추가하는데 필요한 비용
        q (int): 블록 한 개를 제거하는데 필요한 비용
        return (int): 블록을 맞추는데 필요한 비용의 최솟값
    """
    arr = []
    tot = 0
    for i in range(len(land)):
        for j in range(len(land[0])):
            arr.append(land[i][j])
            tot += land[i][j]
    arr.sort()
    # 첫번째 항에 대하여 계산하기
    s = (tot - arr[0] * len(arr)) * q
    last = arr[0]
    answer = s
    for i in range(1, len(arr)):
        if arr[i] == last:
            continue
        up = (arr[i] - last) * p * i
        down = (arr[i] - last) * q * (len(arr) - i)
        # 현재 바닥 비용에서 up을 더하고, down을 빼줘야 한다.
        s += up - down
        answer = min(s, answer)
        last = arr[i]
    return answer


if __name__ == "__main__":
    land = [[4, 4, 3], [3, 2, 2], [2, 1, 0]]
    p = 5
    q = 3
    print(solution(land, p, q))