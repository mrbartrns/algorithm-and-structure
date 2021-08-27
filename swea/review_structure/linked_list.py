# linked_list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curn = self.head
            while curn:
                curn = curn.next
            curn = Node(data)

    def get_data_index(self, data):
        curn = self.head
        idx = 0
        while curn:
            if idx == curn.idx:
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insert_node_at_index(self, idx, data):
        curn = self.head
        prevn = None
        cur_i = 0
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = Node(data)
                self.head.next = nextn
            else:
                self.head = Node(data)
        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                curn += 1
            if cur_i == idx:
                node = Node(data)
                node.next = curn
                prevn.next = node
            else:
                return -1

    def insert_node_at_data(self, key, data):
        idx = self.get_data_index(key)
        if idx >= 0:
            self.insert_node_at_index(idx, data)

    def delete_node_at_index(self, idx):
        curn = self.head
        prevn = None
        nextn = self.head.next
        cur_i = 0
        if idx == 0:
            self.head = nextn
        else:
            while cur_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
            if cur_i == idx:
                prevn.next = nextn

    def clear(self):
        self.head = None

    def __repr__(self):
        curn = self.head
        string = ""
        while curn:
            string += curn.idx
            if curn.next:
                string += "->"
            curn = curn.next
        return string
