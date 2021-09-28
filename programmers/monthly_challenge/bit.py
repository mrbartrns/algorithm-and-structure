# 두개 이하로 다른 비트


def solution(numbers):
    answer = []
    for number in numbers:
        if not (number & 1):
            answer.append(number + 1)
        else:
            idx = 1
            while True:
                if not (number & (1 << idx)):
                    number |= 1 << idx
                    number ^= 1 << (idx - 1)
                    answer.append(number)
                    break
                idx += 1
    return answer


if __name__ == "__main__":
    numbers = [2, 7]
    print(solution(numbers))