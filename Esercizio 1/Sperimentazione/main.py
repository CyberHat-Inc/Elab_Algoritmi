from bst import BST
from avl import AVL
from ordered_list import OrderedList

#TODO commentare il codice

tree = OrderedList()


for val in [10, 5, 15, 3, 7, 12, 20]:
    tree.insert(val)

tree.print()

print("----")

#tree.delete(5)

tree.print()
print("----")

print(tree.select(5))
print(tree.rank(15))