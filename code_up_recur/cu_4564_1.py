import sys


def get_score_memo(k, arr, step, location):
    if k >= 0 and arr[k] != 0:
        return arr[k]
    elif k == 1:
        arr[k] = 1
        return arr[k]


n = 7
arr = [0, 13, 1, 15, 27, 29, 21, 20]