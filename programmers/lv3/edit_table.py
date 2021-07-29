# [카카오] 표 편집
class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data


def solution(n, k, cmds):
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
            op = command[0]
            if op == "D":
                for _ in range(number):
                    cur_node = cur_node.next
            else:
                for _ in range(number):
                    cur_node = cur_node.prev
        else:
            if cmd == "C":
                prev = cur_node.prev
                nxt = cur_node.next
                deleted.append(cur_node)
                state[cur_node.data] = "X"
                if nxt:
                    nxt.prev = prev
                if prev:
                    prev.next = nxt
                if nxt:
                    cur_node = nxt
                else:
                    cur_node = prev
            else:
                restore = deleted.pop()
                prev = restore.prev
                nxt = restore.next
                if prev:
                    prev.next = restore
                if nxt:
                    nxt.prev = restore
                state[restore.data] = "O"
    answer = "".join(state)
    return answer


if __name__ == "__main__":
    n = 8
    k = 2
    cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(n, k, cmds))