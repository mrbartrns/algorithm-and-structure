# 불량 사용자
def solution(user_id, banned_id):
    visited = set()
    state_arr = []
    backtrack(0, len(banned_id), visited, state_arr, user_id, banned_id)
    return len(state_arr)


def backtrack(idx: int, max_cnt: int, visited: set, state_arr: list, user_id: list, banned_id: list):
    if idx == max_cnt:
        if visited not in state_arr:
            state_arr.append(visited.copy())
        return

    for i in range(len(user_id)):
        if i in visited:
            continue
        if len(user_id[i]) != len(banned_id[idx]):
            continue
        banned = list(banned_id[idx])
        for j in range(len(banned)):
            if banned[j] == "*":
                banned[j] = user_id[i][j]

        if banned == list(user_id[i]):
            visited.add(i)
            backtrack(idx + 1, max_cnt, visited, state_arr, user_id, banned_id)
            visited.remove(i)


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
