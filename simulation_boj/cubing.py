# BOJ 5373
import sys

si = sys.stdin.readline
"""
루빅스 큐브: 3차원 퍼즐 -> 각 면에 있는 아홉개의 작은 정육면체들의 색이 동일해야 함
각 면을 양방향으로 90도 회전 가능 -> 회전을 마친 후에는 다른 면을 만들 수 있음
루빅스 큐브가 모두 풀린 상태에서 시작
돌리는 방법이 순서대로 주어질 때, 모두 돌린다음 가장 윗면의 색을 구하는 문제
n: 큐브를 돌린 횟수
큐브를 돌리는 방법 + 시계방향 - 시계반대
"""

COLOR = ['w', 'r', 'b', 'y', 'o', 'g']


# (0, 3), (1, 4), (2, 5)면은 서로 마주보는 면
# 0: 윗면 1, 2, 4, 5: 옆면 3: 아랫면
def copy(op):
    if op[0] == "U" or op[0] == "D":
        d1, d2, d4, d5 = [], [], [], []
        for i in range(3):
            if op[0] == "U":
                d1.append(cube[1][0][i])
                d2.append(cube[2][0][i])
                d4.append(cube[4][0][i])
                d5.append(cube[5][0][i])
            else:
                d1.append(cube[1][2][i])
                d2.append(cube[2][2][i])
                d4.append(cube[4][2][i])
                d5.append(cube[5][2][i])
        return d1, d2, d4, d5
    elif op[0] == "F" or op[0] == "B":
        d0, d2, d3, d5 = [], [], [], []
        for i in range(3):
            if op[0] == "F":
                d0.append(cube[0][2][i])
                d2.append(cube[2][i][0])
                d3.append(cube[3][2][i])
                d5.append(cube[5][i][2])
            else:
                d0.append(cube[0][0][i])
                d2.append(cube[2][i][2])
                d3.append(cube[3][0][i])
                d5.append(cube[5][i][0])
        return d0, d2, d3, d5
    elif op[0] == "L" or op[0] == "R":
        d0, d1, d3, d4 = [], [], [], []
        for i in range(3):
            if op[0] == "L":
                d0.append(cube[0][i][0])
                d1.append(cube[1][i][0])
                d3.append(cube[3][i][2])
                d4.append(cube[4][i][2])
            else:
                d0.append(cube[0][i][2])
                d1.append(cube[1][i][2])
                d3.append(cube[3][i][0])
                d4.append(cube[4][i][0])
        return d0, d1, d3, d4


def rotate_current_face(face, op):
    new_face = []
    if op == "+":
        for j in range(3):
            temp = []
            for i in range(2, -1, -1):
                temp.append(face[i][j])
            new_face.append(temp)
    else:
        for j in range(2, -1, -1):
            temp = []
            for i in range(3):
                temp.append(face[i][j])
            new_face.append(temp)
    return new_face


def rotate(op):
    if op[0] == "U":
        d1, d2, d4, d5 = copy(op)
        # cube[0] = rotate_current_face(cube[0], op[1])
        new_face = rotate_current_face(cube[0], op[1])
        for i in range(3):
            for j in range(3):
                cube[0][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[1][0][i] = d2[i]
                cube[2][0][i] = d4[i]
                cube[4][0][i] = d5[i]
                cube[5][0][i] = d1[i]
            else:
                cube[1][0][i] = d5[i]
                cube[2][0][i] = d1[i]
                cube[4][0][i] = d2[i]
                cube[5][0][i] = d4[i]
    elif op[0] == "D":
        d1, d2, d4, d5 = copy(op)
        # print(d1, d2, d4, d5)
        # cube[3] = rotate_current_face(cube[3], op[1])
        new_face = rotate_current_face(cube[3], op[1])
        for i in range(3):
            for j in range(3):
                cube[3][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[1][2][i] = d5[i]
                cube[2][2][i] = d1[i]
                cube[4][2][i] = d2[i]
                cube[5][2][i] = d4[i]
            else:
                cube[1][2][i] = d2[i]
                cube[2][2][i] = d4[i]
                cube[4][2][i] = d5[i]
                cube[5][2][i] = d1[i]
    elif op[0] == "F":
        d0, d2, d3, d5 = copy(op)
        # cube[1] = rotate_current_face(cube[1], op[1])
        new_face = rotate_current_face(cube[1], op[1])
        for i in range(3):
            for j in range(3):
                cube[1][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[0][2][i] = d5[2 - i]
                cube[3][2][i] = d2[i]
                cube[2][i][0] = d0[i]
                cube[5][i][2] = d3[2 - i]
            else:
                cube[0][2][i] = d2[i]
                cube[3][2][i] = d5[2 - i]
                cube[2][i][0] = d3[i]
                cube[5][i][2] = d0[2 - i]
    elif op[0] == "B":
        d0, d2, d3, d5 = copy(op)
        # cube[4] = rotate_current_face(cube[4], op[1])
        new_face = rotate_current_face(cube[4], op[1])
        for i in range(3):
            for j in range(3):
                cube[4][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[0][0][i] = d2[i]
                cube[3][0][i] = d5[2 - i]
                cube[2][i][2] = d3[i]
                cube[5][i][0] = d0[2 - i]
            else:
                cube[0][0][i] = d5[2 - i]
                cube[3][0][i] = d2[i]
                cube[2][i][2] = d0[i]
                cube[5][i][0] = d3[2 - i]
    elif op[0] == "L":
        # cube[5] = rotate_current_face(cube[5], op[1])
        new_face = rotate_current_face(cube[5], op[1])
        d0, d1, d3, d4 = copy(op)
        for i in range(3):
            for j in range(3):
                cube[5][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[0][i][0] = d4[2 - i]
                cube[1][i][0] = d0[i]
                cube[3][i][2] = d1[2 - i]
                cube[4][i][2] = d3[i]
            else:
                cube[0][i][0] = d1[i]
                cube[1][i][0] = d3[2 - i]
                cube[3][i][2] = d4[i]
                cube[4][i][2] = d0[2 - i]
    elif op[0] == "R":
        # cube[2] = rotate_current_face(cube[2], op[1])
        new_face = rotate_current_face(cube[2], op[1])
        d0, d1, d3, d4 = copy(op)
        for i in range(3):
            for j in range(3):
                cube[2][i][j] = new_face[i][j]
        for i in range(3):
            if op[1] == "+":
                cube[0][i][2] = d1[i]
                cube[1][i][2] = d3[2 - i]
                cube[3][i][0] = d4[i]
                cube[4][i][0] = d0[2 - i]
            else:
                cube[0][i][2] = d4[2 - i]
                cube[1][i][2] = d0[i]
                cube[3][i][0] = d1[2 - i]
                cube[4][i][0] = d3[i]


t = int(si())

for _ in range(t):
    cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]
    rotation_number = int(si())
    rotation = list(si().split())
    for c in rotation:
        rotate(c)
        # for i in range(6):
        #     print(cube[i])
        # print()
    for i in range(3):
        for j in range(3):
            print(COLOR[cube[0][i][j]], end="")
        print()
