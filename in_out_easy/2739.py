import sys


MONTHLY_CALENDER = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = {1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT", 0: "SUN"}


def get_days(m, d):
    days = 0
    for i in range(m):
        days += MONTHLY_CALENDER[i]
    days += d
    return DAYS[days % 7]


m, d = map(int, sys.stdin.readline().split())
sys.stdout.write(get_days(m, d))