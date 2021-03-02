# 스킬트리
from collections import deque

# 순서가 정해져있을때 스택 또는 큐 고려하기
def solution(skill, skill_trees):
    is_in = set(list(skill))
    cnt = 0
    for i in range(len(skill_trees)):
        flag = True
        skill_que = deque(list(skill))
        tree_que = deque(list(skill_trees[i]))
        while skill_que and tree_que:
            c = tree_que.popleft()
            if c in is_in:
                s = skill_que.popleft()
                if c != s:
                    flag = False

            if not flag:
                break
        if flag:
            cnt += 1
    return cnt


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))