import copy
import sys

def fill_empty_cell_4(a):
    cell = [1, 2, 3, 4]
    k = 0
    for i in range(0, 16):
        # a[i] = int(input())
        if a[i] == 0:
            a[i] = copy.copy(cell)
            k += 3
    return k


def check_columns_4(a, i, k):
    j = i
    for _ in range(1, 5):
        j += 4
        if j > 15:
            j -= 16
        k = remove_cell_value(a[j], i, a, k)
    return k


def check_str_4(a, i, k):
    j = i
    for _ in range(1, 5):
        j += 1
        if j > 15:
            j -= 4
        if j // 4 == i // 4:
            k = remove_cell_value(a[j], i, a, k)
    return k


def remove_cell_value(cell_value, num_of: int, a, k):
    # функция удаления значения из клетки
    try:
        if cell_value in a[num_of]:
            a[num_of].remove(cell_value)
            k -= 1
    except TypeError:
        sys.stdout.write(".")
    return k