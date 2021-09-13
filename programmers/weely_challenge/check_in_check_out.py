# 입실 퇴실


def solution(enter, leave):
    answer = [0] * len(enter)
    table = [[0, 0, 0] for _ in range(len(enter))]
    for i in range(len(enter)):
        table[enter[i] - 1][0] = i
        table[enter[i] - 1][2] = enter[i]
    for i in range(len(leave)):
        table[leave[i] - 1][1] = i
    table.sort(key=lambda x: (x[1], x[0], x[2]))
    dp = [[0 for _ in range(len(enter) + 1)] for _ in range(len(enter) + 1)]
    for i in range(len(enter)):
        for j in range(i + 1, len(enter)):
            m1 = table[i][2]
            m2 = table[j][2]


if __name__ == "__main__":
    enter = [1, 4, 2, 3]
    leave = [2, 1, 3, 4]
    print(solution(enter, leave))
