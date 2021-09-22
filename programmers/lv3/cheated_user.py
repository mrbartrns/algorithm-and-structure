# [카카오] 불량 사용자
def is_match(user, cheated_user):
    for i in range(len(user)):
        if cheated_user[i] == "*":
            continue
        if cheated_user[i] != user[i]:
            return False
    return True


def dfs(idx, user_id, banned_id, visited: set, answer: list):
    if idx == len(banned_id):
        if visited not in answer:
            answer.append(visited.copy())
        return
    for i in range(len(user_id)):
        if user_id[i] in visited:
            continue
        if len(user_id[i]) != len(banned_id[idx]):
            continue
        if is_match(user_id[i], banned_id[idx]):
            visited.add(user_id[i])
            dfs(idx + 1, user_id, banned_id, visited, answer)
            visited.remove(user_id[i])


def solution(user_id, banned_id):
    answer = []
    dfs(0, user_id, banned_id, set(), answer)
    return len(answer)


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id, banned_id))