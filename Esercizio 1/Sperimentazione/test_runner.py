import csv

import os_bst
from os_bst import OSBST
from os_avl import OSAVL
from os_ordered_list import OSOrderedList

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

def save_csv(file_name, rows):
    with open(f'results/{file_name}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(['n', 'struttura', 'media'])
        writer.writerows(rows)

def test_casual_input(size, iterations):
    rows = []

    max_seq = random_values(size * iterations)

    for i in range(iterations):
        x = size * (i + 1)
        seq = max_seq[:x]

        insert_elements(OSBST, seq)


    time_os_ordered_list = []
    time_os_bst = []
    time_os_avl = []

    save_csv

def main():
    size = 1300
    iterations = 20
    test_casual_input()


main()