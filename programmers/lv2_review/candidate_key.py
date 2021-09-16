def solution(relation):
    pk = []
    for i in range(1, 1 << len(relation[0])):
        history = []
        for j in range(len(relation)):
            temp = []
            for k in range(len(relation[0])):
                current_key = 1 << k
                if i & current_key:
                    temp.append(relation[j][k])
            if temp not in history:
                history.append(temp)
        if len(history) == len(relation):
            check = True
            for key in pk:
                if key & i == key:
                    check = False
                    break
            if check:
                pk.append(i)
    print(pk)


if __name__ == "__main__":
    relation = [[1, 2], [2, 3]]
    print(solution(relation))
    # print((3,) in (3, 2))
