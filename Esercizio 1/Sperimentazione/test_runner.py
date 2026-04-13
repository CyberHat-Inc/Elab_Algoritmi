from os_bst import OSBST
from os_avl import OSAVL
from os_ordered_list import OSOrderedList
from plot_results import save_csv
from plot_results import plot

import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import math
import sys

sys.setrecursionlimit(10 ** 9)

def random_values(size):
    return random.choices(range(1, 1_000_001), k=size)

def ordered_values(size):
    return list(range(size))

def insert_elements(struct, seq):
    for i in seq:
        struct.insert(i)

def test_casual_input(size, iterations):
    test_name = 'test_casual_input'
    rows = []
    os_bst = OSBST()
    os_avl = OSAVL()
    os_ordered_list = OSOrderedList()

    max_seq = random_values(size * iterations)

    for i in range(iterations):
        x = size * (i + 1)
        seq = max_seq[:x]

        start = timer()
        insert_elements(os_bst, seq)
        end = timer()
        rows.append(['OS_BST', x, end - start])

        start = timer()
        insert_elements(os_avl, seq)
        end = timer()
        rows.append(['OS_AVL', x, end - start])

        start = timer()
        insert_elements(os_ordered_list, seq)
        end = timer()
        rows.append(['OS_LIST', x, end - start])

    save_csv(test_name, rows)
    plot(test_name)

def test_ordered_input(size, iterations):
    test_name = 'test_linear_input'
    rows = []
    os_bst = OSBST()
    os_avl = OSAVL()
    os_ordered_list = OSOrderedList()

    max_seq = ordered_values(size * iterations)

    for i in range(iterations):
        x = size * (i + 1)
        seq = max_seq[:x]

        start = timer()
        insert_elements(os_bst, seq)
        end = timer()
        rows.append(['OS_BST', x, end - start])

        start = timer()
        insert_elements(os_avl, seq)
        end = timer()
        rows.append(['OS_AVL', x, end - start])

        start = timer()
        insert_elements(os_ordered_list, seq)
        end = timer()
        rows.append(['OS_LIST', x, end - start])

    save_csv(test_name, rows)
    plot(test_name)

def run_all_tests(size, iterations):
    test_casual_input(size, iterations)
    test_ordered_input(size, iterations)

def main():
    size = 100
    iterations = 16
    run_all_tests(size, iterations)



main()