class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node: Node):
        if not self.head:
            self.head = node
        else:
            curn = self.head
            while curn.next:
                curn = curn.next
            curn.next = node

    def get_data_index(self, data):
        idx = 0
        curn = self.head
        while curn:
            if curn.data == data:
                return idx
            idx += 1
            curn = curn.next
        return -1

    def insert_node_at_index(self, idx: int, node: Node):
        curn = self.head
        prevn = None
        curn_i = 0

        if idx == 0:
            if not self.head:
                self.head = node
            else:
                nextn = self.head
                self.head = node
                self.head.next = nextn
        else:
            while curn_i < idx:
                # 길이가 5일때 5인 인덱스를 넣어도 맨 마지막에 넣을 수 있다
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                curn_i += 1

            if curn_i == idx:
                prevn.next = node
                node.next = curn
            else:
                return -1

    def insert_node_at_data(self, data, node: Node):
        index = self.get_data_index(data)
        if index >= 0:
            self.insert_node_at_index(index, node)
        else:
            return -1

    def delete_at_index(self, idx):
        # 위에서 정의하는 이유는 바로 아래에서 쓰기 위함임
        curn = self.head
        prevn = None
        nextn = self.head.next
        curn_i = 0

        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next  # nextn의 next가 없어도 상관 없다
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1

    def clear(self):
        self.head = None

    def __repr__(self):
        string = ""
        curn = self.head
        while curn:
            string += str(curn.data)
            if curn.next:
                string += " -> "
            curn = curn.next
        return string


if __name__ == "__main__":
    s1 = SinglyLinkedList()
    s1.append(Node(1))
    s1.append(Node(2))
    s1.append(Node(3))
    s1.append(Node(4))
    s1.append(Node(5))
    print(s1)
    s1.insert_node_at_index(5, Node(6))
    print(s1)
    print(s1.get_data_index(6))