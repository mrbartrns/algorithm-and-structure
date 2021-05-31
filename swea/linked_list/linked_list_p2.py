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

    def get_data_index(self, data):
        curn = self.head
        idx = 0
        while curn:  # curn이 None이 아닌 동안
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1  # 조건에 맞는 데이터가 없을 때 반환

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

    def insert_node_at_data(self, data, node: Node):
        index = self.get_index_data(data)
        if index >= 0:
            self.insert_node_at_index(index, node)
        else:
            return -1

    def length(self):
        counter = 0
        curn = self.head
        while curn:
            curn = curn.next
            counter += 1
        return counter

    def clear(self):
        self.head = None

    def print_reverse(self, num):
        cur_i = 0
        length = self.length()
        string = ""
        real_num = num if length > num else length
        while cur_i < real_num:
            string += str(self.get_index_data(length - cur_i - 1))
            if cur_i < real_num - 1:
                string += " "
            cur_i += 1
        return string

    def __repr__(self):
        string = ""
        curn = self.head
        while curn:
            string += str(curn.data)
            if curn.next:
                string += " "
            curn = curn.next
        return string


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    linked_list = SinglyLinkedList()
    for _ in range(m):
        arr = [int(x) for x in input().split()]
        length = linked_list.length()
        if length == 0:
            for k in arr:
                linked_list.append(Node(k))
        else:
            l = 0
            flag = False
            while l < length:
                if linked_list.get_index_data(l) > arr[0]:
                    for p in range(len(arr)):
                        linked_list.insert_node_at_index(l + p, Node(arr[p]))
                    flag = True
                    break
                l += 1
            if not flag:
                for p in arr:
                    linked_list.append(Node(p))
    print(f"#{i + 1} {linked_list.print_reverse(10)}")
