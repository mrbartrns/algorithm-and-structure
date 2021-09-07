# [카카오] 신규 아이디 추천
from collections import deque


def solution(new_id):
    allowed_special_characters = set(["-", ".", "_"])
    # step 1
    new_id = new_id.lower()

    # step 2, step 3
    temp_id = []
    for c in new_id:
        if ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
            temp_id.append(c)
            continue
        if c in allowed_special_characters:
            temp_id.append(c)
    que = deque()
    for c in temp_id:
        if que and (que[-1] == "." and c == "."):
            continue
        que.append(c)

    if que and que[0] == ".":
        que.popleft()
    if que and que[-1] == ".":
        que.pop()

    if not que:
        que.append("a")

    while len(que) >= 16:
        que.pop()
    if que and que[-1] == ".":
        que.pop()
    while len(que) <= 2:
        last_word = que[-1]
        que.append(last_word)
    return "".join(que)


if __name__ == "__main__":
    new_id = "z-+.^."
    print(solution(new_id))