"""
n이 주어지면 트리를 만든 다음에 루트노드와 n // 2 노드를 출력
크기가 고정되어있는 완전한 이진트리이므로, 리스트로 구현하는게 빠르고 편함
부모노드는 왼쪽 자식노드보다는 커야하고, 오른쪽 자식노드보다는 작아야 함
>> 재귀함수로 구현하기

오름차순으로 트리를 나타내기 위해서는 중위순회방식을 썼음. 따라서 중위순회하면서 가장 왼쪽의 노드부터 탐색하여 숫자를 바꿈
"""

# list를 이용하여 완전 이진트리 구현
# n = 6
# arr = [x for x in range(n + 1)]
# arr[0] = None
# print(arr)
# counts = [1]


# 기본적으로 중위순회와 알고리즘이 완전히 동일하다.
def sort_tree(tree, counts, n=1):
    if n < len(tree):
        sort_tree(tree, counts, 2 * n)
        tree[n] = counts[0]
        counts[0] += 1
        sort_tree(tree, counts, 2 * n + 1)


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [int(x) for x in range(n + 1)]
    counts = [1]
    sort_tree(arr, counts)
    print(f"#{tc + 1} {arr[1]} {arr[n // 2]}")
