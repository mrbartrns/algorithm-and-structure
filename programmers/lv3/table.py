# [카카오] 표 편집


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


def solution(n, k, cmds):
    """cmds에 따라 표를 조작하는 함수

    Args:
        n (int): [description]
        k (int): [description]
        cmds ([type]): [description]
    """
    linked_list = [Node(0)]
    state = ["O"] * n
    removed = []
    for i in range(1, n):
        node = Node(i)
        prev = linked_list[i - 1]
        prev.next = node
        node.prev = prev
        linked_list.append(node)

    cur_node = linked_list[k]
    for cmd in cmds:
        if len(cmd) >= 2:
            op, number = cmd.split(" ")
            if op == "D":
                for _ in range(int(number)):
                    cur_node = cur_node.next
            else:
                for _ in range(int(number)):
                    cur_node = cur_node.prev
        else:
            if cmd == "C":
                removed.append(cur_node)
                state[cur_node.data] = "X"
                prev = cur_node.prev
                nxt = cur_node.next
                if prev:
                    prev.next = nxt
                if nxt:
                    nxt.prev = prev

                if nxt:
                    cur_node = nxt
                else:
                    cur_node = prev
            else:
                restore = removed.pop()
                state[restore.data] = "O"
                prev = restore.prev
                nxt = restore.next
                if prev:
                    prev.next = restore
                if nxt:
                    nxt.prev = restore
    return "".join(state)


if __name__ == "__main__":
    n = 8
    k = 2
    cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(n, k, cmds))