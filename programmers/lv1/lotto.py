# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    s = set(win_nums)
    matched = 0
    unknown = 0
    for n in lottos:
        if n == 0:
            unknown += 1
        elif n in s:
            matched += 1
    return [
        7 - matched - unknown if matched + unknown > 0 else 6,
        7 - matched if matched > 0 else 6,
    ]


if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))