# 폰켓몬
def solution(nums):
    n = -1
    cnt = 0
    nums.sort()
    for i in range(len(nums)):
        if n != nums[i]:
            n = nums[i]
            cnt += 1
        if cnt == len(nums) // 2:
            break

    return cnt