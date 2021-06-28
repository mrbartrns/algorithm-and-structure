# 불량 사용자
def solution(user_id, banned_id):
    visited = set()
    state_arr = []
    return backtrack(0, user_id, banned_id, visited, state_arr)


def backtrack(idx, user_id, banned_id, visited, state_arr):
    max_cnt = len(banned_id)
    cnt = 0
    if idx == max_cnt:
        if visited not in state_arr:
            state_arr.append(visited.copy())
            return 1
        return 0
    for i in range(len(user_id)):
        if i in visited:
            continue

        if len(banned_id[idx]) != len(user_id[i]):
            continue
        same = True
        for j in range(len(banned_id[idx])):
            if banned_id[idx][j] == "*":
                continue
            if banned_id[idx][j] != user_id[i][j]:
                same = False
                break

        if same:
            visited.add(i)
            cnt += backtrack(idx + 1, user_id, banned_id, visited, state_arr)
            visited.remove(i)

    return cnt


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
