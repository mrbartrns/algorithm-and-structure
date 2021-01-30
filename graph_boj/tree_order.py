# BOJ 1991
import sys

si = sys.stdin.readline
"""
tree = [
    None,
    "A",
    "B",
    "C",
    "D",
    None,
    "E",
    "F",
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "G",
]
"""

n = int(si())
tree = [None] * (2 ** n)
for _ in range(n):
    root, c1, c2 = si().split()
    if not tree[1]:
        tree[1] = root
        if 2 < len(tree) and c1 != ".":
            tree[2] = c1
        if 3 < len(tree) and c2 != ".":
            tree[3] = c2
    else:
        for i in range(len(tree)):
            if tree[i] == root:
                if 2 * i < len(tree) and c1 != ".":
                    tree[2 * i] = c1
                if 2 * i + 1 < len(tree) and c2 != ".":
                    tree[2 * i + 1] = c2


def pre_order(root):
    print(tree[root], end="")
    if root * 2 < len(tree) and tree[root * 2]:
        pre_order(root * 2)
    if root * 2 + 1 < len(tree) and tree[root * 2 + 1]:
        pre_order(root * 2 + 1)


def inorder(root):
    if root * 2 < len(tree) and tree[root * 2]:
        inorder(root * 2)
    print(tree[root], end="")
    if root * 2 + 1 < len(tree) and tree[root * 2 + 1]:
        inorder(root * 2 + 1)


def post_order(root):
    if root * 2 < len(tree) and tree[root * 2]:
        post_order(root * 2)
    if root * 2 + 1 < len(tree) and tree[root * 2 + 1]:
        post_order(root * 2 + 1)
    print(tree[root], end="")


pre_order(1)
print()
inorder(1)
print()
post_order(1)