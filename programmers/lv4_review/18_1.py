# 쿠키 구입

def solution(cookie):
    partial_sum = psum(cookie)
    answer = 0
    for mid in range(1, len(partial_sum)):
        left = 0
        right = len(partial_sum) - 1
        while left < mid < right:
            lsum = partial_sum[mid] - partial_sum[left]
            rsum = partial_sum[right] - partial_sum[mid]
            if lsum > rsum:
                left += 1
            elif lsum < rsum:
                right -= 1

            if lsum == rsum:
                answer = max(answer, lsum)
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
    cookie = [1, 1, 2, 3]
    print(solution(cookie))
