# 최댓값과 최솟값
def solution(s):
    ans = [None, None]
    arr = s.split(" ")
    arr.sort(key=lambda x: int(x))
    ans[0] = arr[0]
    ans[1] = arr[-1]
    return " ".join(ans)


s = "1 2 3 4"
print(solution(s))