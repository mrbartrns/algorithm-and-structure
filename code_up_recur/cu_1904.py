import sys


def get_odd_number(start, end):
    if end >= start:
        if end % 2 == 1:
            get_odd_number(start, end - 2)
            print(end, end=" ")
        else:
            get_odd_number(start, end - 1)


a, b = map(int, sys.stdin.readline().split())
get_odd_number(a, b)