# BOJ 1991
import sys

si = sys.stdin.readline


tree = {}
n = int(si())
for _ in range(n):
    root, c1, c2 = si().split()
    tree[root] = tree.get(root, []) + [c1, c2]


def pre_order(root):
    print(root, end="")
    if tree[root][0] != ".":
        pre_order(tree[root][0])
    if tree[root][1] != ".":
        pre_order(tree[root][1])


def inorder(root):
    if tree[root][0] != ".":
        inorder(tree[root][0])
    print(root, end="")
    if tree[root][1] != ".":
        inorder(tree[root][1])


def post_order(root):
    if tree[root][0] != ".":
        post_order(tree[root][0])
    if tree[root][1] != ".":
        post_order(tree[root][1])
    print(root, end="")


pre_order("A")
print()
inorder("A")
print()
post_order("A")