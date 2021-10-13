# 교점에 별 만들기

INF = 987654321


def get_boundary(crossed_points):
    min_y, min_x, max_y, max_x = INF, INF, -INF, -INF
    for a, b in crossed_points:
        min_y = min(min_y, a)
        max_y = max(max_y, a)
        min_x = min(min_x, b)
        max_x = max(max_x, b)
    return min_y, min_x, max_y, max_x


def get_integer_crossed_point(lines):
    ret = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            a1, b1, c1 = lines[i]
            a2, b2, c2 = lines[j]
            if a1 != 0 and a2 != 0 and (b1 != 0 or b2 != 0):
                if a1 < 0:
                    a1, b1, c1 = -a1, -b1, -c1
                if a2 < 0:
                    a2, b2, c2 = -a2, -b2, -c2
                gcd = get_gcd(a1, a2)
                lcm = get_lcm(a1, a2, gcd)
                a1, b1, c1 = lcm, lcm // a1 * b1, lcm // a1 * c1
                a2, b2, c2 = lcm, lcm // a2 * b2, lcm // a2 * c2
                _, b3, c3 = a1 - a2, b1 - b2, c1 - c2
                if (c3 / b3) - (c3 // b3) != 0:
                    continue
                y = -(c3 // b3)
                x = -(c1 + b1 * y) // a1
                ret.append((-y, x))
            elif b1 != 0 and b2 != 0 and (a1 != 0 or a2 != 0):
                if b1 < 0:
                    a1, b1, c1 = -a1, -b1, -c1
                if b2 < 0:
                    a2, b2, c2 = -a2, -b2, -c2
                gcd = get_gcd(b1, b2)
                lcm = get_lcm(b1, b2, gcd)
                a1, b1, c1 = lcm // b1 * a1, lcm, lcm // b1 * c1
                a2, b2, c2 = lcm // b2 * a2, lcm, lcm // b2 * c2
                a3, _, c3 = a1 - a2, b1 - b2, c1 - c2
                if (c3 / a3) - (c3 // a3) != 0:
                    continue
                x = -(c3 // a3)
                y = -(c2 + a2 * x) // b2
                ret.append((-y, x))
            else:
                if (a1 == 0 and a2 == 0) or (b1 == 0 and b2 == 0):
                    continue
                if a1 == 0:
                    if c1 / b1 - int(c1 / b1) != 0:
                        continue
                    if c2 / a2 - int(c2 / a2) != 0:
                        continue
                    y = c1 // b1
                    x = c2 // a2
                    ret.append((-y, x))
                else:
                    if c1 / a1 - int(c1 / a1) != 0:
                        continue
                    if c2 / b2 - int(c2 / b2) != 0:
                        continue
                    x = c1 // a1
                    y = c2 // b2
                    ret.append((-y, x))

    return ret


def get_lcm(a, b, gcd):
    return a * b // gcd


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return get_gcd(b, a % b)


def solution(lines):
    answer = []
    ret = get_integer_crossed_point(lines)
    min_y, min_x, max_y, max_x = get_boundary(ret)
    board = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for a, b in ret:
        board[a - min_y][b - min_x] = "*"
    for i in range(len(board)):
        answer.append("".join(board[i]))
    return answer


if __name__ == "__main__":
    lines = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
    print(solution(lines))
