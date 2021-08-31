# [카카오] 자동완성

import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, a):
        self.char = a
        self.cnt = 0
        self.next = []


def solution(words):
    answer = 0
    alphabets = [Node(chr(i + ord('a'))) for i in range(26)]
    for word in words:
        node = alphabets[ord(word[0]) - ord('a')]
        dfs(node, 1, word)
    for i in range(len(alphabets)):
        answer += get_count(alphabets[i])
    return answer


def dfs(node, idx, word):
    node.cnt += 1

    if idx == len(word):
        return

    check = False
    for next_node in node.next:
        if next_node.char == word[idx]:
            check = True
            dfs(next_node, idx + 1, word)
            break
    if not check:
        next_node = Node(word[idx])
        node.next.append(next_node)
        dfs(next_node, idx + 1, word)


def get_count(node):
    answer = 0
    answer += node.cnt
    if node.cnt > 1:
        for next_node in node.next:
            answer += get_count(next_node)
    return answer


if __name__ == '__main__':
    words = ["go", "gone", "guild"]
    print(solution(words))
