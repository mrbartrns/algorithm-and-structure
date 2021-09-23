# [카카오] 메뉴 리뉴얼

table = {}


def backtrack(idx, tot, ret, string, visited):
    if idx == tot:
        table[ret] = table.get(ret, 0) + 1
        return

    for i in range(visited, len(string)):
        backtrack(idx + 1, tot, ret + string[i], string, i + 1)


def solution(orders, course):
    answer = []
    table_list = []
    for order in orders:
        table_list.append(sorted(list(order)))
    for cnt in course:
        max_value = 0
        for order in table_list:
            backtrack(0, cnt, "", order, 0)
        for key in table:
            if table[key] > max_value:
                max_value = table[key]
        if max_value < 2:
            continue
        for key in table:
            if table[key] == max_value:
                answer.append(key)
        table.clear()
    answer.sort()
    return answer


if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]
    print(solution(orders, course))