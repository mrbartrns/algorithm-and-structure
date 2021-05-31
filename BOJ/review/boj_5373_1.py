# BOJ 5373 (큐빙)
import sys

sys.stdin = open("input.txt", "r")
si = sys.stdin.readline


def rotate_current_face(front: int, rotate_d: str) -> list:
    """rotate cube's current face

    Args:
        front (int): cube's face index what I need to rotate
        rotate_d (str): rotate direction, "+" is clockwise, "-" is counter clockwise;

    Returns:
        list: new - rotated current face of cube
    """
    ret = []
    if rotate_d == "+":  # clockwise
        for j in range(3):
            temp = []
            for i in range(2, -1, -1):
                temp.append(cube[front][i][j])
            ret.append(temp)
    elif rotate_d == "-":  # counter-clockwise
        for j in range(2, -1, -1):
            temp = []
            for i in range(3):
                temp.append(cube[front][i][j])
            ret.append(temp)
    return ret


def copy(front: str) -> list:
    """copy cube's cube when rotate that influenced by rotation

    Args:
        front (str): cube's face index

    Returns:
        list: return copied cubes
    """
    if front == "U":
        # 1, 2, 3, 4번 면의 윗쪽이 영향을 받음
        d1, d2, d3, d4 = [], [], [], []
        for i in range(3):
            d1.append(cube[1][0][i])
            d2.append(cube[2][0][i])
            d3.append(cube[3][0][i])
            d4.append(cube[4][0][i])
        return d1, d2, d3, d4

    elif front == "B":
        d0, d2, d3, d5 = [], [], [], []
        for i in range(3):
            d0.append(cube[0][0][i])
            d2.append(cube[2][i][2])
            d3.append(cube[3][i][0])
            d5.append(cube[5][0][i])
        return d0, d2, d3, d5

    elif front == "R":
        d0, d1, d4, d5 = [], [], [], []
        for i in range(3):
            d0.append(cube[0][i][2])
            d1.append(cube[1][i][0])
            d4.append(cube[4][i][2])
            d5.append(cube[5][i][0])
        return d0, d1, d4, d5

    elif front == "L":
        d0, d1, d4, d5 = [], [], [], []
        for i in range(3):
            d0.append(cube[0][i][0])
            d1.append(cube[1][i][2])
            d4.append(cube[4][i][0])
            d5.append(cube[5][i][2])
        return d0, d1, d4, d5

    elif front == "F":
        d0, d2, d3, d5 = [], [], [], []
        for i in range(3):
            d0.append(cube[0][2][i])
            d2.append(cube[2][i][0])
            d3.append(cube[3][i][2])
            d5.append(cube[5][2][i])
        return d0, d2, d3, d5

    elif front == "D":
        d1, d2, d3, d4 = [], [], [], []
        for i in range(3):
            d1.append(cube[1][2][i])
            d2.append(cube[2][2][i])
            d3.append(cube[3][2][i])
            d4.append(cube[4][2][i])
        return d1, d2, d3, d4


def rotate(op: str):
    """display cube's status after rotated

    Args:
        op (str): op is 2 word string. first word is one of the "F", "B", "U", "D", "L", "R"
        and second word is direction of rotation, "+", "-"
    """
    if op[0] == "U":
        new_face = rotate_current_face(0, op[1])

        for i in range(3):
            for j in range(3):
                cube[0][i][j] = new_face[i][j]

        d1, d2, d3, d4 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[1][0][i] = d3[i]
                cube[2][0][i] = d1[i]
                cube[3][0][i] = d4[i]
                cube[4][0][i] = d2[i]
            else:  # counter-clockwise
                cube[1][0][i] = d2[i]
                cube[2][0][i] = d4[i]
                cube[3][0][i] = d1[i]
                cube[4][0][i] = d3[i]

    elif op[0] == "B":
        new_face = rotate_current_face(1, op[1])

        for i in range(3):
            for j in range(3):
                cube[1][i][j] = new_face[i][j]

        d0, d2, d3, d5 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[0][0][i] = d2[i]
                cube[2][i][2] = d5[i]
                cube[3][i][0] = d0[2 - i]
                cube[5][0][i] = d3[2 - i]
            else:  # counter-clockwise
                cube[0][0][i] = d3[2 - i]
                cube[2][i][2] = d0[i]
                cube[3][i][0] = d5[2 - i]
                cube[5][0][i] = d2[i]

    elif op[0] == "R":
        new_face = rotate_current_face(2, op[1])

        for i in range(3):
            for j in range(3):
                cube[2][i][j] = new_face[i][j]

        d0, d1, d4, d5 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[0][i][2] = d4[i]
                cube[1][i][0] = d0[2 - i]
                cube[4][i][2] = d5[2 - i]
                cube[5][i][0] = d1[i]
            else:  # counter-clockwise
                cube[0][i][2] = d1[2 - i]
                cube[1][i][0] = d5[i]
                cube[4][i][2] = d0[i]
                cube[5][i][0] = d4[2 - i]

    elif op[0] == "L":
        new_face = rotate_current_face(3, op[1])
        
        for i in range(3):
            for j in range(3):
                cube[3][i][j] = new_face[i][j]

        d0, d1, d4, d5 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[0][i][0] = d1[2 - i]
                cube[1][i][2] = d5[i]
                cube[4][i][0] = d0[i]
                cube[5][i][2] = d4[2 - i]
            else:  # counter-clockwise
                cube[0][i][0] = d4[i]
                cube[1][i][2] = d0[2 - i]
                cube[4][i][0] = d5[2 - i]
                cube[5][i][2] = d1[i]

    elif op[0] == "F":
        new_face = rotate_current_face(4, op[1])

        for i in range(3):
            for j in range(3):
                cube[4][i][j] = new_face[i][j]

        d0, d2, d3, d5 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[0][2][i] = d3[2 - i]
                cube[2][i][0] = d0[i]
                cube[3][i][2] = d5[2 - i]
                cube[5][2][i] = d2[i]
            else:  # counter-clockwise
                cube[0][2][i] = d2[i]
                cube[2][i][0] = d5[i]
                cube[3][i][2] = d0[2 - i]
                cube[5][2][i] = d3[2 - i]

    elif op[0] == "D":
        new_face = rotate_current_face(5, op[1])
        for i in range(3):
            for j in range(3):
                cube[5][i][j] = new_face[i][j]

        d1, d2, d3, d4 = copy(op[0])
        for i in range(3):
            if op[1] == "+":  # clockwise
                cube[1][2][i] = d2[i]
                cube[2][2][i] = d4[i]
                cube[3][2][i] = d1[i]
                cube[4][2][i] = d3[i]
            else:  # counter-clockwise
                cube[1][2][i] = d3[i]
                cube[2][2][i] = d1[i]
                cube[3][2][i] = d4[i]
                cube[4][2][i] = d2[i]


t = int(si())
for _ in range(t):
    cube = [
        [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],
        [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],
        [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]],
        [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],
        [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],
        [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],
    ]
    n = int(si())
    operators = list(si().split())
    for i in range(n):
        op = operators[i]
        rotate(op)
    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end="")
        print()
