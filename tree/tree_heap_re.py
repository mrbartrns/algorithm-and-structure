# binary tree
class Node:
    def __init__(self, data):
        """
        node constructor
        binary tree의 노드는 왼쪽노드와 오른쪽노드에 관련된 정보를 가지고 있어야 한다.
        """
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        """
        binary tree의 size를 구하는 함수
        size는 왼쪽사이즈와 오른쪽 사이즈를 더하는 재귀함수로 구현할 수 있다.
        """
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1

    def depth(self):
        """
        binary tree의 depth를 구하는 함수
        depth는 재귀적으로 구현이 가능하다.
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.left.depth() if self.right else 0
        return left_depth + 1 if left_depth > right_depth else right_depth + 1

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        """
        binary tree constructor
        binary tree의 초기값은 오직 root만 지정한다.
        """
        self.root = None

    def size(self):
        return self.root.size() if self.root else 0

    def depth(self):
        return self.root.depth() if self.root else 0

    # insert function
    def insert(self, data):
        """
        data를 삽입하는 함수
        help function
        """
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        """
        실질적으로 node의 root, left, right에 삽입해주는 함수
        사용시에는 insert함수만 사용할 것
        """
        # 재귀함수의 base case
        if node is None:
            node = Node(data)

        else:
            if data <= node.data:
                node.left = self._insert_value(
                    node.left, data
                )  # 현재 node의 left, right를 지정한다면, 계속해서 하위 depth로 내려가게되고 자동으로 재귀함수는 종료된다.

            else:
                node.right = self._insert_value(
                    node.right, data
                )  # 현재 node의 left, right를 지정한다면, 계속해서 하위 depth로 내려가게되고 자동으로 재귀함수는 종료된다.

        return node

    # find function
    def find(self, key):
        """
        data를 찾는 함수
        help function
        input: key
        return: boolean if node.data == key or node is None
        """
        return self._find_value(self.root, key)

    def _find_value(self, node, key):
        """
        data를 찾기 위한 재귀함수
        사용시에는 find 함수만 사용할 것
        input: node, key (init: self.root)
        return: recursive function
        """
        if not node:
            return False
        elif node.data == key:
            return True

        else:
            if key < node.data:
                return self._find_value(node.left, key)
            else:
                return self._find_value(node.right, key)

    # get minimum function
    def get_min_value(self, node):
        """
        minimum value를 찾는 function
        return: minimum value of binary search tree
        """
        if not node.left:
            return node.data
        else:
            return self.get_min_value(node.left)

    # delete function
    def delete(self, key):
        """
        값을 찾아서 delete 하는 help function
        input: key
        return: boolean
        """
        self.root = self._delete_value(self.root, key)
        return self.root is not None

    def _delete_value(self, node, key):
        """
        find and delete value recursively
        if node hasn't value or not node: return none
        if node hasn't child node: return none
        if node has only one child: return child
        if node has two childs: find minimum value and change it,
        and delete minimum value
        """
        if not node:
            return None

        # case1. key < node.data
        if key < node.data:
            node.left = self._delete_value(
                node.left, key
            )  # key가 현재 데이터보다 작다면, 노드의 왼쪽방향의 자식노드를 탐색후 제거
            return node  # return된 값을 전달하기 위해 필요함

        # case2. key > node.data
        elif key > node.data:
            node.right = self._delete_value(
                node.right, key
            )  # key가 현재 데이터보다 크다면, 노드의 오른쪽 방향의 자식노드를 탐색후 제거
            return node  # return된 값을 전달하기 위해 필요함

        # case3. key == node.data
        else:

            # case1. current node has no child
            if not node.left and not node.right:  # 자식노드를 가지고 있을 때
                return None  # node = None

            # case2. current node has only left child
            elif node.left and not node.right:
                return node.left

            # case3. current node has only right child
            elif node.right and not node.left:
                return node.right

            # case4. current node has two childs
            else:
                # 현재 노드의 오른쪽 노드의 가장 왼쪽 값을 제거한다.
                min_node = self.get_min_value(node.right)
                node.data = min_node.data
                node.right = self._delete_value(
                    node.right, min_node.data
                )  # node 오른쪽 서브트리를 재구성한다.
                return node  # 바뀐 노드의 정보를 반환

    # preorder, inorder, preorder
    def preorder(self, node):
        """
        preorder는 루트부터 탐색하여 왼쪽, 아래쪽으로 서브트리를 내려가며 탐색
        """
        if node is not None:
            print(node.data, end=" ")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def inorder(self, node):
        """
        오름차순으로 탐색
        """
        if node is not None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end=" ")
            if node.right:
                self.inorder(node.right)

    def postorder(self, node):
        """
        아래 자식부터 탐색
        """
        if node is not None:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.data, end=" ")


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1  # 맨 마지막 인덱스
        while idx > 1:
            if self.heap[idx] > self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = (
                    self.heap[idx // 2],
                    self.heap[idx],
                )
                idx //= 2
            else:
                break

    def delete(self):
        """
        heap 자료구조는 오직 root(index가 1인 항목)만 삭제할 수 있다.
        """
        if len(self.heap) > 1:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop()
            self.heapify(1)

    def heapify(self, idx):
        """
        루트 노드에 가장 큰 값을 배치하는 함수
        """
        left = idx * 2
        right = (idx * 2) + 1
        largest = idx
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if idx != largest:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.heapify(largest)

    def __str__(self):
        return str(self.heap[1:])


if __name__ == "__main__":
    """
    bst = BST()
    data = [11, 5, 10, 4, 9, 3, 8, 1, 2, 6, 7]
    for i in data:
        bst.insert(i)
    bst.delete(3)
    bst.inorder(bst.root)
    print()
    print(bst.find(5))

    # print(bst.root.left, bst.root.right)
    """
    heap = MaxHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    print(heap)
    heap.delete()
    print(heap)