# BOJ 1062
import sys

"""
# 그냥 된다 안된다를 검증하는 것이 아니라 최댓값을 구해야 함
def can_read(word, added):
    # 기저사례
    if k - (len(known) + len(added)) < 0:
        return False

    if not word:
        return True

    # 작업의 분할 및 반복
    if word[0] not in known:
        added.append(word[0])
    # 부분해를 반환받아 전체 해 구성
    if can_read(word[1:], added):
        return True
    return False


def solve(known, counts, stack):
    if stack == len(words):
        return

    if counts not in answer:
        answer.append(counts)

    for y in range(len(words)):
        if not flag[y]:
            flag[y] = True
            added = []
            # 단어를 읽을 수 있는지 확인. 읽을 수 있다면, 1을 반환 및 다음단계로 이동 > 현재 스택으로 돌아왔을 때, 다시 1을 제거
            temp = list(words[y])
            val = 1 if can_read(words[y], added) else 0
            has_added = added[:]
            if has_added:
                known.extend(temp)

            solve(known, counts + val, stack + 1)
            if has_added:
                for _ in range(len(temp)):
                    known.pop()
            # 단어를 읽을 수 없을 때에는,
            flag[y] = False


# 첫 단어가 틀렸을 때 첫 단어의 값을 모두 빼야 함
"""
"""
answer = []
added = []
i_s = []
k = 6
words = ["b", "", "e", "e"]
flag = [False for _ in range(len(words))]
solve(known, 0, 0)
print(answer)
"""
"""
n, k = map(int, sys.stdin.readline().split())
known = ["a", "n", "t", "y", "c"]
words = []
answer = []
for _ in range(n):
    word = sys.stdin.readline()
    word = word[4:-5]
    words.append(word)
flag = [False for _ in range(len(words))]
solve(known, 0, 0)
answer.sort()
sys.stdout.write(str(answer[-1]))
"""


def dfs(idx, cnt):

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for c in word:
                if not learn[ord(c) - ord("a")]:
                    break
            else:
                read_cnt += 1
        answer[0] = max(answer[0], read_cnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


n, k = map(int, sys.stdin.readline().split())
if k < 5 or k == 26:
    print(0 if k < 5 else n)
    sys.exit(0)

words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
answer = [0]
learn = [False] * 26

for c in ("a", "c", "y", "n", "t"):
    learn[ord(c) - ord("a")] = True
dfs(0, 0)
print(answer[0])

"""
from sys import stdin, exit


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord("a")]:
                    break
            else:
                read_cnt += 1
        answer = max(answer, read_cnt) if answer else read_cnt
        return

    for y in range(idx, 26):
        if not learn[y]:
            learn[y] = True
            dfs(y, cnt + 1)
            learn[y] = False


if __name__ == "__main__":
    answer = None
    n, k = map(int, stdin.readline().split())

    if k < 5 or k == 26:
        print(0 if k < 5 else n)
        exit(0)

    words = [set(stdin.readline().rstrip()) for _ in range(n)]
    learn = [False] * 26

    for c in ("a", "c", "y", "n", "t"):
        learn[ord(c) - ord("a")] = True

    dfs(0, 0)
    print(answer)
    """