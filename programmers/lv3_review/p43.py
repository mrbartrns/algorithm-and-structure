class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data


def solution(n, k, cmds):
    # head 값을 지정해 주는 과정을 생략하기 위하여 먼저 list에 head값을 넣어서 사용한다.
    node_list = [Node(0)]
    deleted = []
    state = ["O"] * n
    for i in range(1, n):
        node = Node(i)
        prev = node_list[i - 1]
        prev.next = node
        node.prev = prev
        node_list.append(node)

    cur_node = node_list[k]
    for cmd in cmds:
        command = cmd.split(" ")
        if len(command) > 1:
            number = int(command[1])
            if command[0] == "D":
                for _ in range(number):
                    cur_node = cur_node.next
            else:
                for _ in range(number):
                    cur_node = cur_node.prev
        else:
            if cmd == "C":
                deleted.append(cur_node)
                prev = cur_node.prev
                nxt = cur_node.next
                state[cur_node.data] = "X"
                if nxt:
                    nxt.prev = prev
                if prev:
                    prev.next = nxt  # None이어도 상관 없음
                if nxt:
                    cur_node = nxt
                else:
                    cur_node = prev
            else:
                r = deleted.pop()
                prev = cur_node.prev
                nxt = cur_node.next
                if prev:
                    prev.next = cur_node
                if nxt:
                    nxt.prev = cur_node
                state[r.data] = "O"
    return "".join(state)


if __name__ == "__main__":
    n = 8
    k = 2
    cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    print(solution(n, k, cmds))