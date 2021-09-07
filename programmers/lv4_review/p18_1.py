def psum(cookie):
    s = 0
    ret = []
    for i in range(len(cookie)):
        ret.append(s)
        s += cookie[i]
    ret.append(s)
    return ret


def solution(cookie):
    partial_sum = psum(cookie)
    print(partial_sum)
    answer = 0
    for m in range(len(partial_sum)):
        left = 0
        right = len(partial_sum) - 1
        while left <= m <= right:
            lsum = partial_sum[m] - partial_sum[left]
            rsum = partial_sum[right] - partial_sum[m]
            if lsum > rsum:
                left += 1
            elif lsum < rsum:
                right -= 1
            else:
                answer = max(answer, lsum)
                break
    return answer


if __name__ == "__main__":
    cookie = [1, 1, 2, 3]
    print(solution(cookie))