# [카카오] 후보키


def is_unique(pk, row, col, relation):
    ret = set()
    for i in range(row):
        string = ""
        for j in range(col):
            if pk & (1 << j):
                string += relation[i][j]
        if string in ret:
            return False
        ret.add(string)
    return True


def is_minimal(pk, pks):
    for key in pks:
        if key & pk == key:
            return False
    return True


class PK:
    def __init__(self) -> None:
        self.pks = set()

    def is_unique(self, pk, relation):
        ret = set()
        row = len(relation)
        col = len(relation[0])
        for i in range(row):
            string = ""
            for j in range(col):
                if pk & (1 << j):
                    string += relation[i][j]
            if string in ret:
                return False
            ret.add(string)
        return True

    def is_minimal(self, pk):
        for key in self.pks:
            if key & pk == key:
                return False
        return True

    # def append(self, item):
    #     self.pks.append(item)
    def add(self, item):
        self.pks.add(item)

    def __getitem__(self, idx):
        return self.pks[idx]

    def __len__(self) -> int:
        return len(self.pks)


def solution(relation):
    pks = []
    row = len(relation)
    col = len(relation[0])
    pks = PK()
    for i in range(1, 1 << col):
        # if not is_minimal(i, pks):
        #     continue
        if not pks.is_minimal(i):
            continue

        # if is_unique(i, row, col, relation):
        #     pks.append(i)
        if pks.is_unique(i, relation):
            pks.add(i)
    return len(pks)


if __name__ == "__main__":
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
    print(solution(relation))
    # print(int("101", 2))
