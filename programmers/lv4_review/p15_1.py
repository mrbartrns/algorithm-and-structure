# [카카오] 자동 완성
import sys

sys.setrecursionlimit(1000001)


class Node:
    def __init__(self, a):
        self.char = a
        self.cnt = 0
        self.next = []

    def __str__(self):
        return self.char


def dfs(node, word, idx):
    node.cnt += 1
    if idx == len(word):
        return

    nxt_node = None
    for nxt in node.next:
        if nxt.char == word[idx]:
            nxt_node = nxt
            break
    if not nxt_node:
        nxt_node = Node(word[idx])
        node.next.append(nxt_node)
    dfs(nxt_node, word, idx + 1)


def get_count(node):
    s = node.cnt
    if node.cnt > 1:
        for nxt in node.next:
            s += get_count(nxt)
    return s


def solution(words):
    alphabets = []
    answer = 0
    for i in range(26):
        alphabets.append(Node(chr(i + ord('a'))))

    for word in words:
        node = alphabets[ord(word[0]) - ord('a')]
        dfs(node, word, 1)

    for i in range(26):
        answer += get_count(alphabets[i])

    return answer


if __name__ == '__main__':
    words = ["abc", "def", "ghi", "jklm"]
    print(solution(words))
