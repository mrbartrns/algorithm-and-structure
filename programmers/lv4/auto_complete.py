# [카카오] 자동완성
import sys

sys.setrecursionlimit(1000001)


class Node:
    def __init__(self, a):
        self.alphabet = a
        self.cnt = 0
        self.nxt = []


def increase(node, word, word_idx):
    node.cnt += 1

    if word_idx == len(word):
        return

    chk = False
    for nxt_node in node.nxt:
        if nxt_node.alphabet == word[word_idx]:
            chk = True
            increase(nxt_node, word, word_idx + 1)
            break
    if not chk:
        nxt_node = Node(word[word_idx])
        node.nxt.append(nxt_node)
        increase(nxt_node, word, word_idx + 1)


def count(node):
    answer = 0
    answer += node.cnt
    if node.cnt > 1:
        for nxt_node in node.nxt:
            answer += count(nxt_node)
    return answer


def solution(words):
    answer = 0
    node_idx = [Node(chr(ord('a') + i)) for i in range(26)]
    for word in words:
        node = node_idx[ord(word[0]) - ord('a')]
        increase(node, word, 1)
    for i in range(26):
        if node_idx[i].cnt > 0:
            answer += count(node_idx[i])
    return answer


if __name__ == '__main__':
    words = ["word", "war", "warrior", "world"]
    print(solution(words))
