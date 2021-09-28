# [카카오] 메뉴 리뉴얼
table = {}


def backtrack(idx, nxt, count, arr, ret):
    if idx == count:
        table[ret] = table.get(ret, 0) + 1
        return
    for i in range(nxt, len(arr)):
        backtrack(idx + 1, i + 1, count, arr, ret + arr[i])


def solution(orders, course):
    for s in orders:
        arr = list(s)
        arr.sort()
        for i in range(2, len(arr) + 1):
            backtrack(0, 0, i, arr, "")
    counts = {}
    answer = []
    for key in table:
        if len(key) in course:
            counts[len(key)] = max(table[key], counts.get(len(key), 0))
    for key in table:
        if len(key) not in counts:
            continue
        if table[key] < 2:
            continue
        if table[key] == counts[len(key)]:
            answer.append(key)
    answer.sort()
    return answer


if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]
    print(solution(orders, course))
