# [카카오] 표 편집
class Node:
    def __init__(self, idx):
        self.prev = None
        self.next = None
        self.idx = idx


def solution(n, k, cmds):
    linked_list = [Node(0)]
    removed = []
    state = ["O"] * n
    for i in range(1, n):
        node = Node(i)
        prev = linked_list[i - 1]
        prev.next = node
        node.prev = prev
        linked_list.append(node)

    cur_node = linked_list[k]
    for cmd in cmds:
        if len(cmd) > 1:
            op, num = cmd.split(' ')
            if op == "D":
                for _ in range(int(num)):
                    cur_node = cur_node.next
            elif op == "U":
                for _ in range(int(num)):
                    cur_node = cur_node.prev
        else:
            if cmd == "C":
                removed.append(cur_node)
                state[cur_node.idx] = "X"
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
                state[restore.idx] = "O"
                prev = restore.prev
                nxt = restore.next
                if prev:
                    prev.next = restore
                if nxt:
                    nxt.prev = restore
    return "".join(state)


if __name__ == '__main__':
    n = 8
    k = 2
    cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(n, k, cmds))
