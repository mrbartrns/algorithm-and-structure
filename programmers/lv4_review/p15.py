# [카카오] 자동 완성
import sys

sys.setrecursionlimit(1000001)


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.cnt = 0
        self.next = []


def solution(words):
    answer = 0
    alphabets = [Node(i) for i in range(26)]
    for word in words:
        dfs(alphabets[ord(word[0]) - ord('a')], 1, word)
    for i in range(len(alphabets)):
        if alphabets[i].cnt > 0:
            answer += get_count(alphabets[i])
    return answer


def get_count(node):
    answer = 0
    answer += node.cnt
    if node.cnt > 1:
        for nxt_node in node.next:
            answer += get_count(nxt_node)
    return answer


def dfs(node, idx, word):
    node.cnt += 1

    if idx == len(word):
        return

    chk = False
    for nxt_node in node.next:
        if nxt_node.idx == ord(word[idx]) - ord('a'):
            chk = True
            dfs(nxt_node, idx + 1, word)
            break
    if not chk:
        nxt_node = Node(ord(word[idx]) - ord('a'))
        node.next.append(nxt_node)
        dfs(nxt_node, idx + 1, word)


if __name__ == '__main__':
    words = ["word", "war", "warrior", "world"]
    print(solution(words))
