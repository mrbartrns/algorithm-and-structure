# 쿠키 구입
def solution(cookie):
    answer = 0
    partial_sum = psum(cookie)
    for mid in range(1, len(partial_sum)):
        left = 0
        right = len(partial_sum) - 1
        while left < mid < right:
            if partial_sum[mid] - partial_sum[left] < partial_sum[right] - partial_sum[mid]:
                right -= 1
            elif partial_sum[mid] - partial_sum[left] > partial_sum[right] - partial_sum[mid]:
                left += 1

            if partial_sum[mid] - partial_sum[left] == partial_sum[right] - partial_sum[mid]:
                answer = max(answer, partial_sum[mid] - partial_sum[left])
                break

    return answer


def psum(arr):
    ret = [0]
    s = 0
    for i in range(len(arr)):
        s += arr[i]
        ret.append(s)
    return ret


if __name__ == '__main__':
    cookie = [1, 2, 4, 5]
    print(solution(cookie))
