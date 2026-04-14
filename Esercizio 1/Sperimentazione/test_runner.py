import math
import numpy as np
import random
import sys
from timeit import default_timer as timer

from os_avl import OSAVL
from os_bst import OSBST
from os_ordered_list import OSOrderedList
from plot_results import plot
from plot_results import save_csv

sys.setrecursionlimit(10 ** 9)


def random_values(size):
    return random.sample(range(1, 10_000_001), k=size)


def ordered_values(size):
    return list(range(size))


def insert_elements(struct, seq):
    for i in seq:
        struct.insert(i)


def delete_elements(struct, seq):
    for i in seq:
        struct.delete(i)


def rank_elements(struct, seq):
    for i in seq:
        struct.rank(i)


def select_elements(struct, seq):
    for i in seq:
        struct.select(i)


def test_casual_input(size, steps, repetitions):
    test_name = 'test_casual_input'
    rows = []

    max_seq = random_values(size * steps)

    for i in range(steps):
        x = size * (i + 1)
        seq = max_seq[:x]

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            start = timer()
            insert_elements(os_bst, seq)
            end = timer()
            times_os_bst.append(end - start)

            start = timer()
            insert_elements(os_avl, seq)
            end = timer()
            times_os_avl.append(end - start)

            start = timer()
            insert_elements(os_ordered_list, seq)
            end = timer()
            times_os_ordered_list.append(end - start)

        rows.append(['OS_BST', x, np.mean(times_os_bst)])
        rows.append(['OS_AVL', x, np.mean(times_os_avl)])
        rows.append(['OS_Ordered_List', x, np.mean(times_os_ordered_list)])

    save_csv(test_name, rows)
    plot(test_name)


def test_ordered_input(size, steps, repetitions):
    test_name = 'test_linear_input'
    rows = []

    max_seq = ordered_values(size * steps)

    for i in range(steps):
        x = size * (i + 1)
        seq = max_seq[:x]

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            start = timer()
            insert_elements(os_bst, seq)
            end = timer()
            times_os_bst.append(end - start)

            start = timer()
            insert_elements(os_avl, seq)
            end = timer()
            times_os_avl.append(end - start)

            start = timer()
            insert_elements(os_ordered_list, seq)
            end = timer()
            times_os_ordered_list.append(end - start)

        rows.append(['OS_BST', x, np.mean(times_os_bst)])
        rows.append(['OS_AVL', x, np.mean(times_os_avl)])
        rows.append(['OS_Ordered_List', x, np.mean(times_os_ordered_list)])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_deletion(size, steps, repetitions):
    test_name = 'test_casual_deletion'
    rows = []

    max_seq = random_values(size * steps)

    for i in range(steps):
        x = size * (i + 1)

        seq = max_seq[:x]
        del_seq = random.sample(seq, x //2)

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst, max_seq[:x])
            insert_elements(os_avl,  max_seq[:x])
            insert_elements(os_ordered_list, max_seq[:x])

            start = timer()
            delete_elements(os_bst, del_seq)
            end = timer()
            times_os_bst.append(end - start)

            start = timer()
            delete_elements(os_avl, del_seq)
            end = timer()
            times_os_avl.append(end - start)

            start = timer()
            delete_elements(os_ordered_list, del_seq)
            end = timer()
            times_os_ordered_list.append(end - start)

        rows.append(['OS_BST', x, np.mean(times_os_bst)])
        rows.append(['OS_AVL', x, np.mean(times_os_avl)])
        rows.append(['OS_Ordered_List', x, np.mean(times_os_ordered_list)])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_ranking(size, steps, repetitions):
    test_name = 'test_casual_rank'
    rows = []

    max_seq = random_values(size * steps)

    for i in range(steps):
        x = size * (i + 1)
        seq = max_seq[:x]
        rank_seq = random.sample(seq, x // 2)

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst,  max_seq[:x])
            insert_elements(os_avl, max_seq[:x])
            insert_elements(os_ordered_list,  max_seq[:x])

            start = timer()
            rank_elements(os_bst, rank_seq)
            end = timer()
            times_os_bst.append(end - start)

            start = timer()
            rank_elements(os_avl, rank_seq)
            end = timer()
            times_os_avl.append(end - start)

            start = timer()
            rank_elements(os_ordered_list, rank_seq)
            end = timer()
            times_os_ordered_list.append(end - start)

        rows.append(['OS_BST', x, np.mean(times_os_bst)])
        rows.append(['OS_AVL', x, np.mean(times_os_avl)])
        rows.append(['OS_Ordered_List', x, np.mean(times_os_ordered_list)])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_selection(size, steps, repetitions):
    test_name = 'test_casual_selection'
    rows = []

    max_seq = random_values(size * steps)

    for i in range(steps):
        x = size * (i + 1)
        select_seq = [random.randint(1, x) for _ in range(x // 2)]

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst,  max_seq[:x])
            insert_elements(os_avl,  max_seq[:x])
            insert_elements(os_ordered_list,  max_seq[:x])

            start = timer()
            select_elements(os_bst, select_seq)
            end = timer()
            times_os_bst.append(end - start)

            start = timer()
            select_elements(os_avl, select_seq)
            end = timer()
            times_os_avl.append(end - start)

            start = timer()
            select_elements(os_ordered_list, select_seq)
            end = timer()
            times_os_ordered_list.append(end - start)

        rows.append(['OS_BST', x, np.mean(times_os_bst)])
        rows.append(['OS_AVL', x, np.mean(times_os_avl)])
        rows.append(['OS_Ordered_List', x, np.mean(times_os_ordered_list)])

    save_csv(test_name, rows)
    plot(test_name)


def run_all_tests(size, steps, repetitions):
    test_casual_input(size, steps, repetitions)
    test_ordered_input(size, steps, repetitions)
    test_casual_deletion(size, steps, repetitions)
    test_casual_ranking(size, steps, repetitions)
    test_casual_selection(size, steps, repetitions)


def main():
    size = 500
    steps = 20
    repetitions = 5
    run_all_tests(size, steps, repetitions)


main()
