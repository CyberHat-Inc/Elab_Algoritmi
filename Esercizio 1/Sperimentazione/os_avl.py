# Implemento le statistiche d'ordine dinamiche utilizzando un albero AVL e aggiungendo l'attributo size.
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1
        self.size = 1


class OSAVL:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_size(self, node):
        if node is None:
            return 0
        return node.size

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update(self, node):
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self._update(z)
        self._update(y)
        return y

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update(z)
        self._update(y)
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self._update(node)
        balance = self._get_balance(node)

        # Caso Left-Left
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Caso Left-Right
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Caso Right-Right
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Caso Right-Left
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        self._update(node)
        balance = self._get_balance(node)

        # stessi 4 casi dell'insert
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print(self):
        self.inorder_tree_walk()

    def inorder_tree_walk(self):
        self._inorder_tree_walk(self.root)

    def _inorder_tree_walk(self, node):
        if node is not None:
            self._inorder_tree_walk(node.left)
            print(node.key)
            self._inorder_tree_walk(node.right)

    # Aggiungo le funzioni per implementare le statistiche d'ordine dinamiche
    def select(self, i):
        return self._select(self.root, i)

    def _select(self, node, i):
        if node is None:
            return None
        t = self._get_size(node.left)
        if i == t + 1:
            return node.key
        elif i <= t:
            return self._select(node.left, i)
        else:
            return self._select(node.right, i - t - 1)

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self._get_size(node.left) + self._rank(node.right, key)
        else:
            return self._get_size(node.left) + 1
