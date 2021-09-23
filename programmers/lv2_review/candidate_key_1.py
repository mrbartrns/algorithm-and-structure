# [카카오] 후보키
class PK:
    def __init__(self) -> None:
        self.pks = set()

    def is_minimum(self, key):
        for pk in self.pks:
            if pk & key == pk:
                return False
        return True

    def is_unique(self, key, relation):
        ret = set()
        row = len(relation)
        col = len(relation[0])
        for i in range(row):
            string = ""
            for j in range(col):
                if key & (1 << j):
                    string += relation[i][j]
            if string in ret:
                return False
            ret.add(string)
        return True

    def add(self, item):
        self.pks.add(item)

    def __len__(self):
        return len(self.pks)


def solution(relation):
    col = len(relation[0])
    pk = PK()
    for i in range(1, 1 << col):
        if not pk.is_minimum(i):
            continue
        if pk.is_unique(i, relation):
            pk.add(i)
    return len(pk)


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