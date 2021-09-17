# [카카오] 자동완성
import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.cnt = 0
        self.next = []

    def __str__(self) -> str:
        return self.data


def get_sum(node):
    ret = node.cnt
    if node.cnt > 1:
        for nxt in node.next:
            ret += get_sum(nxt)
    return ret


def append_word(idx, node, word):
    node.cnt += 1

    if idx == len(word):
        return

    nxt_node = None
    for nxt in node.next:
        if word[idx] == nxt.data:
            nxt_node = nxt
            break
    if not nxt_node:
        nxt_node = Node(word[idx])
        node.next.append(nxt_node)
    append_word(idx + 1, nxt_node, word)


def solution(words):
    node_list = []
    answer = 0
    for i in range(26):
        node_list.append(Node(chr(i + ord("a"))))
    for word in words:
        append_word(1, node_list[ord(word[0]) - ord("a")], word)
    for i in range(26):
        answer += get_sum(node_list[i])
    return answer


if __name__ == "__main__":
    words = ["word", "war", "warrior", "world"]
    print(solution(words))