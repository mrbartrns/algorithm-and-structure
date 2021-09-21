# [카카오] 키패드 누르기
locations = [
    (3, 1),
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
]


def solution(numbers, hand):
    answer = []
    left = (3, 0)
    right = (3, 2)
    for number in numbers:
        ny, nx = locations[number]
        if nx == 0:
            answer.append("L")
            left = (ny, nx)
        elif nx == 2:
            answer.append("R")
            right = (ny, nx)
        else:
            distance_from_left = abs(ny - left[0]) + abs(nx - left[1])
            distance_from_right = abs(ny - right[0]) + abs(nx - right[1])
            if distance_from_left < distance_from_right:
                answer.append("L")
                left = (ny, nx)
            elif distance_from_left > distance_from_right:
                answer.append("R")
                right = (ny, nx)
            else:
                if hand == "left":
                    answer.append("L")
                    left = (ny, nx)
                else:
                    answer.append("R")
                    right = (ny, nx)
    return "".join(answer)


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))
