# 파일명 정렬
def solution(files):
    arr = []
    for name in files:
        temp = solve(name)
        arr.append(temp)

    arr.sort(key=lambda x: (x[0], x[1]))
    new = list(map(lambda x: x[3], arr))
    return new


def solve(name):
    arr = []
    head, num, tail = "", "", ""
    idx = -1
    n_idx = -1
    number = True
    # head
    for i in range(len(name)):
        if name[i] >= "0" and name[i] <= "9":
            arr.append(head)
            break
        else:
            head += name[i].lower()
            idx = i

    # number
    for i in range(idx + 1, len(name)):
        if "0" <= name[i] and name[i] <= "9":
            n_idx = i
            num += name[i]
        else:
            arr.append(int(num))
            number = False
            break
    if number:
        arr.append(int(num))

    # tail
    tail = name[n_idx + 1 :]
    arr.append(tail)

    # name
    arr.append(name)

    return arr


files = ["foo9.txt", "foo010bar020.zip", "F-15"]
print(solution(files))