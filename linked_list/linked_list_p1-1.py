# 링크드 리스트를 이용한 숫자 추가
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

    def append(self, node):
        curn = self.head
        if not self.head:
            self.head = node
        else:
            while curn.next:
                curn = curn.next
            curn.next = node

    def get_index_data(self, idx):
        curn = self.head
        curn_i = 0
        if self.head:
            while curn:
                if curn_i == idx:
                    return curn.data
                curn_i += 1
                curn = curn.next
        return -1

    def insert_node_at_index(self, idx, node):
        prevn = None
        curn = self.head
        curn_i = 0
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            while curn_i < idx:
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

    def __repr__(self):
        string = "["
        curn = self.head
        while curn:
            string += str(curn.data)
            if curn.next:
                string += ", "
            curn = curn.next
        string += "]"
        return string


t = int(input())
for i in range(t):
    arr_len, add_counts, idx = map(int, input().split())
    arr = [int(x) for x in input().split()]
    linked_list = SinglyLinkedList()
    for j in arr:
        linked_list.append(Node(j))

    for _ in range(add_counts):
        index, num = map(int, input().split())
        # linked_list.insert_node_at_index(index, Node(num))
    print(linked_list)
    print(f"#{i + 1} {linked_list.get_index_data(idx)}")