class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def _find(self, node, key):
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def _successor(self, node):
        if node.right is not None:
            return self._min(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y

    def insert(self, key):
        z = BSTNode(key)

        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, key):
        z = self._find(self.root, key)
        if z is None:
            return

        # Caso 1
        if z.left is None and z.right is None:
            if z.parent is None:
                self.root = None
            elif z == z.parent.left:
                z.parent.left = None
            else:
                z.parent.right = None
        # Caso 2
        elif z.left is None or z.right is None:
            child = z.left if z.right is None else z.right
            child.parent = z.parent
            if z.parent is None:
                self.root = child
            elif z == z.parent.left:
                z.parent.left = child
            else:
                z.parent.right = child
        # Caso 3
        else:
            y = self._successor(z)
            z.key = y.key
            if y == y.parent.left:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            if y.right is not None:
                y.right.parent = y.parent

    # Per prova
    def print(self):
        self.inorder_tree_walk()

    def inorder_tree_walk(self):
        self._inorder_tree_walk(self.root)

    # Lo aggiungo per poter fare delle chiamate ricorsive senza dover passare la radice nel main
    def _inorder_tree_walk(self, x):
        if x is not None:
            self._inorder_tree_walk(x.left)
            print(x.key)
            self._inorder_tree_walk(x.right)

    # Aggiungo le funzioni per implementare le statistiche d'ordine dinamiche
    # Aumento il BST senza aggiungere l'attributo size, mi serve un metodo che tutte le volte conti gli elementi
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def select(self, x):
        return self._select(self.root, x)

    def _select(self, node, i):
        if node is None:
            return None
        t = self._size(node.left)
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
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left) + 1