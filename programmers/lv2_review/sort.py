# [카카오] 파일명 정렬


class Node:
    def __init__(self, file) -> None:
        self.filename = file
        self.head, self.number = self.get_head_and_number(file)

    def get_head_and_number(self, filename):
        head = ""
        number = ""
        for c in filename:
            if ord("0") <= ord(c) <= ord("9"):
                number += c
            elif number and (ord(c) < ord("0") or ord(c) > ord("9")):
                break
            else:
                head += c
        return head.lower(), int(number)

    def __str__(self) -> str:
        return self.filename


def solution(files):
    node_list = []
    for file in files:
        node_list.append(Node(file))
    node_list.sort(key=lambda x: (x.head, x.number))
    return list(map(lambda x: x.filename, node_list))


if __name__ == "__main__":
    files = [
        "F-5 Freedom Fighter",
        "B-50 Superfortress",
        "A-10 Thunderbolt II",
        "F-14 Tomcat",
    ]
    print(solution(files))