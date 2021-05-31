def get_power(n, s):
    if n // 10 == 0:
        return s
    else:
        s += 1
        return get_power(n // 10, s)

s = 0
# print(get_power(1004, 0))

def get_reverse_number(n):
    if n // 10 == 0:
        return n
    else:
        new_n = (n % 10) * (10 ** get_power(n, 0)) + get_reverse_number(n // 10)
        return new_n

# print(get_reverse_number(1004))

###################################################################################

def num_equal(arr, x, c):
    if len(arr) == 1:
        if arr[0] == x:
            c += 1
        return c
    else:
        mid = len(arr) // 2
        left, right = num_equal(arr[:mid], x, c), num_equal(arr[mid:], x, c)
        return left + right

# print(num_equal([1, 2, 4, 4, 5, 4, 2, 4, 4], 4, 0))

seq = 0
def binary_search(arr, n):
    global seq
    if len(arr) <= 1:
        if arr[0] == n:
            return True
        else:
            return False
    else:
        seq += 1
        print(seq)
        mid = len(arr) // 2
        if n < arr[mid]:
            return binary_search(arr[:mid], n)
        elif n > arr[mid]:
            return binary_search(arr[mid:], n)
        else:
            return True

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))

def sum_rec(n):
    if n == 0:
        return 0
    else:
        return n + sum_rec(n - 1)

def sum_loop(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res

# print(sum_loop(5), sum_rec(5))

def seq1(n):
    # if n == 1:
    #     return 12
    if n == 0:
        return 0
    else:
        return n * 10 + 2 + seq1(n - 1)

# print(seq1(2))

def nested_rec(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return nested_rec(n - 1, 1)
    else:
        nested_rec(n - 1, nested_rec(n , m - 1))


def print2n(n):
    if n > 3600:
        return
    else:
        print2n(2 * n)
        print(n)

def print2n_r(n):
    if n < 1:
        return
    else:
        print2n_r(n // 2)
        if n <= 3600:
            print(n)
        

# print2n_r(3600)

def tree(n):
    if n == 1:
        print(1)
    else:
        tree(n - 1)
        print(n)
        tree(n - 1)

# tree(4)

def color(target, pattern, y, x):
    global color_arr
    global flag
    if (y < 0 or y >= len(color_arr)) or ((x < 0 or x >= len(color_arr[0]))):
        return
    # print(color_arr[y][x])
    # if (color_arr[y][x] != target and color_arr[y][x] != pattern) or color_arr[y][x] == 0:
    #     return
    else:
        color_arr[y][x] = pattern
        flag[y][x] = True
        print(color_arr)
        if not flag[y][x - 1]:
            color(target, pattern, y, x - 1)
        if not flag[y][x + 1]:
            color(target, pattern, y, x + 1)
        if not flag[y - 1][x]:
            color(target, pattern, y - 1, x)
        if not flag[y + 1][x]:
            color(target, pattern, y + 1, x)
        flag[y][x] = False

color_arr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

flag = []
for i in range(len(color_arr)):
    temp = []
    for j in range(len(color_arr[0])):
        temp.append(True) if color_arr[i][j] == 0 else temp.append(False)
    flag.append(temp)

# print(flag)
x = 5
y = 3
target = 1
pattern = 2
color(target, pattern, y, x)
print(color_arr)