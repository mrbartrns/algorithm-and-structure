# [카카오] 자동 완성
import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, a) -> None:
        self.alphabet = a
        self.cnt = 0
        self.next = []


def get_sum(node):
    s = node.cnt
    if s > 1:
        for child in node.next:
            s += get_sum(child)
    return s


def dfs(node, word, idx):
    node.cnt += 1
    nxt = None
    if idx == len(word):
        return
    for child in node.next:
        if child.alphabet == word[idx]:
            nxt = child
            break
    if not nxt:
        nxt = Node(word[idx])
        node.next.append(nxt)
    dfs(nxt, word, idx + 1)


def solution(words):
    answer = 0
    node_list = [Node(chr(i + ord("a"))) for i in range(26)]
    for word in words:
        dfs(node_list[ord(word[0]) - ord("a")], word, 1)
    for el in node_list:
        answer += get_sum(el)
    return answer


if __name__ == "__main__":
    words = ["go", "gone", "guild"]
    print(solution(words))