import random
import sys
from timeit import default_timer as timer

import numpy as np

from os_avl import OSAVL
from os_bst import OSBST
from os_ordered_list import OSOrderedList
from plot_results import plot
from plot_results import save_csv


def random_values(size):
    return random.sample(range(1, 10_00_000), k=size)


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


def test_casual_input(size, step, repetitions):
    test_name = 'test_casual_input'
    rows = []

    for i in range(step, size + 1, step):
        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            seq = random_values(i)

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

        rows.append(['OS_BST', i, np.median(times_os_bst) / i])
        rows.append(['OS_AVL', i, np.median(times_os_avl) / i])
        rows.append(['OS_Ordered_List', i, np.median(times_os_ordered_list) / i])

    save_csv(test_name, rows)
    plot(test_name)


def test_ordered_input(size, step, repetitions):
    test_name = 'test_linear_input'
    rows = []

    max_seq = ordered_values(size)

    for i in range(step, size + 1, step):
        seq = max_seq[:i]

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

        rows.append(['OS_BST', i, np.median(times_os_bst) / i])
        rows.append(['OS_AVL', i, np.median(times_os_avl) / i])
        rows.append(['OS_Ordered_List', i, np.median(times_os_ordered_list) / i])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_deletion(size, step, repetitions):
    test_name = 'test_casual_deletion'
    rows = []

    for i in range(step, size + 1, step):
        seq = random_values(i)

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            del_seq = random.sample(seq, i // 2)

            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst, seq)
            insert_elements(os_avl, seq)
            insert_elements(os_ordered_list, seq)

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

        rows.append(['OS_BST', i, np.median(times_os_bst) / (i // 2)])
        rows.append(['OS_AVL', i, np.median(times_os_avl) / (i // 2)])
        rows.append(['OS_Ordered_List', i, np.median(times_os_ordered_list) / (i // 2)])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_ranking(size, step, repetitions):
    test_name = 'test_casual_rank'
    rows = []

    for i in range(step, size + 1, step):
        seq = random_values(i)

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            rank_seq = random.sample(seq, i // 2)

            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst, seq)
            insert_elements(os_avl, seq)
            insert_elements(os_ordered_list, seq)

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

        rows.append(['OS_BST', i, np.median(times_os_bst) / (i // 2)])
        rows.append(['OS_AVL', i, np.median(times_os_avl) / (i // 2)])
        rows.append(['OS_Ordered_List', i, np.median(times_os_ordered_list) / (i // 2)])

    save_csv(test_name, rows)
    plot(test_name)


def test_casual_selection(size, step, repetitions):
    test_name = 'test_casual_selection'
    rows = []

    for i in range(step, size + 1, step):
        seq = random_values(i)
        select_seq = [random.randint(1, i) for _ in range(i // 2)]

        times_os_ordered_list = []
        times_os_bst = []
        times_os_avl = []

        for j in range(repetitions):
            os_bst = OSBST()
            os_avl = OSAVL()
            os_ordered_list = OSOrderedList()

            # Popolo le strutture
            insert_elements(os_bst, seq)
            insert_elements(os_avl, seq)
            insert_elements(os_ordered_list, seq)

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

        rows.append(['OS_BST', i, np.median(times_os_bst) / (i // 2)])
        rows.append(['OS_AVL', i, np.median(times_os_avl) / (i // 2)])
        rows.append(['OS_Ordered_List', i, np.median(times_os_ordered_list) / (i // 2)])

    save_csv(test_name, rows)
    plot(test_name)


def run_all_tests(size, step, repetitions):
    test_casual_input(size, step, repetitions)
    test_ordered_input(size, step, repetitions)
    test_casual_deletion(size, step, repetitions)
    test_casual_ranking(size, step, repetitions)
    test_casual_selection(size, step, repetitions)


def main():
    size = 3000
    step = 100
    repetitions = 15
    run_all_tests(size, step, repetitions)


main()
