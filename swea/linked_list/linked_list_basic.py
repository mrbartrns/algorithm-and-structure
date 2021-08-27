# Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    # constructor, 처음 head는 아무것도 없는 상태이다.
    def __init__(self):
        self.head = None
        self.count = 0

    # 새로운 노드를 링크드 리스트의 마지막에 추가한다.
    def append(self, node):
        if self.head == None:  # 링크드 리스트에 아무것도 없다면
            self.head == node  # 헤드를 노드로 지정한다.
        else:  # 링크드 리스트에 원소가 있다면
            cur = self.head  # 현재 헤드값을 cur 변수에 저장한다.
            while cur.next != None:
                cur = cur.next  # 현재 값에 next의 주소를 저장한다. > 다음의 값을 가리키게 한다
            cur.next = node  # next 값에 현재 node의 참조 주소를 저장한다.

    # 주어진 데이터의 인덱스 반환
    def get_data_index(self, data):
        curn = self.head
        idx = 0
        while curn:  # curn이 None이 아닌 동안
            if curn.idx == data:
                return idx
            curn = curn.next
            idx += 1
        return -1  # 조건에 맞는 데이터가 없을 때 반환

    # 주어진 위치에 데이터 삽입
    def insert_node_at_index(self, idx, node):
        """
        node는 세 가지 방법으로 추가될 수 있다.
        1. 링크드 리스트의 맨 앞
        2. 주어진 인덱스
        3. 링크드 리스트의 맨 마지막
        """

        curn = self.head  # 현재 위치를 헤드로 잡는다.
        prevn = None  # 현재 위치가 헤드라면, 이전에는 아무것도 없다.
        cur_i = 0  # 현재 위치가 헤드일때 인덱스는 0

        # 링크드리스트의 맨 앞에 삽입할 때
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node

        else:
            while cur_i < idx:  # 현재 인덱스가 idx보다 작을동안
                if curn:
                    prevn = curn  # prevn에다가 현재 노드를 저장하고 현재노드에 next값을 할당한다.
                    curn = curn.next
                else:  # 링크드리스트의 맨 마지막일경우 멈춘다.
                    break
                cur_i += 1

            if cur_i == idx:  # 현재 인덱스의 앞에 추가한다.
                node.next = curn  # 현재 노드의 다음값에 curn 값의 참조주소를 추가한다.
                prevn.next = node  # 이전값에는 현재 node의 참조주소를 추가한다.
            else:
                return -1

    def insert_node_at_data(self, data, node):  # 데이터 값을 바탕으로 추가한다.
        index = self.get_data_index(data)
        if index >= 0:
            self.insert_node_at_index(index, node)
        else:
            return -1

    def delete_at_index(self, idx):  # 인덱스 값으로 데이터를 삭제한다.
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:  # 0번째 노드를 삭제(헤드를 삭제)
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn  # 이전값의 next 주소를 현재 다음값으로 바꾼다.

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
