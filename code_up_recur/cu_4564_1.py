import sys


def get_score_memo(k, arr, location):
    if k == 0:
        return 0
    elif k == 1:
        return arr[k]
    elif k == 2:
        return arr[k]
    else:
        location[k] = True
        val = (
            max(
                get_score_memo(k - 1, arr, location)
                if not (location[k] and location[k - 1] and location[k - 2])
                else 0,
                get_score_memo(k - 2, arr, location),
            )
            + arr[k]
        )
        location[k] = False
        return val


# n = 7
# arr = [0, 13, 1, 15, 27, 29, 21, 20]
n = 5
arr = [0, 1, 2, 3, 4, 5]
location = [False] * (n + 1)
print(get_score_memo(n, arr, location))
