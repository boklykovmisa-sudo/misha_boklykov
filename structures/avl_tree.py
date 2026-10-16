class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_right(y):
    x = y.left
    middle = x.right
    x.right = y
    y.left = middle
    update_height(y)
    update_height(x)
    return x


def rotate_left(x):
    y = x.right
    middle = y.left
    y.left = x
    x.right = middle
    update_height(x)
    update_height(y)
    return y


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        update_height(node)
        balance = height(node.left) - height(node.right)
        if balance > 1:
            if key > node.left.key:
                node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1:
            if key < node.right.key:
                node.right = rotate_right(node.right)
            return rotate_left(node)
        return node

    def contains(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            current = current.left if key < current.key else current.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node:
                visit(node.left)
                result.append(node.key)
                visit(node.right)

        visit(self.root)
        return result
