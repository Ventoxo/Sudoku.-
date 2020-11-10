import copy
import sys

'''def fill_empty_cell_4(a):
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
'''


def check_str_9(a, i, k):
    j = i
    for _ in range(0, 9):
        j += 1
        if j > 80:
            j -= 9
        if j // 9 == i // 9:
            try:
                k = remove_cell_value(a[j], i, a, k)
            except IndexError:
                sys.stdout.write(".")
        else:
            j -= 9
    return k


def check_columns_9(a, i, k):
    j = i
    '''print("kek")
    print(j)'''
    for _ in range(0, 9):
        j += 9
        '''print("kek")
        print(j)'''
        if j > 80:
            j -= 81
        '''print("kek")
        print(j)'''
        try:
            k = remove_cell_value(a[j], i, a, k)
        except IndexError:
            sys.stdout.write(".")
    return k


def fill_empty_cell_9(a):
    cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 0
    for i in range(0, 81):
        # a[i] = int(input())
        if a[i] == 0:
            a[i] = copy.copy(cell)
            k += 9
    return k


def check_yadro_9(a, i, k):
    key = 0
    j = i
    for _ in range(0, 9):
        if (j + 1) // 3 == j // 3:
            j += 1
        elif (j + 7) // 27 == i // 27:
            j += 7
        else:
            j -= 20

        try:
            k = remove_cell_value(a[j], i, a, k)
        except IndexError:
            sys.stdout.write(".")
    return k


def abstraction(a, k, i):
    # на случай, если нет решения, например, для сложных судоку
    return k


def remove_cell_value(cell_value, num_of: int, a, k):  # функция удаления значения из клетки
    '''print("a[num_of]")
    print(cell_value, num_of, a, k)'''
    try:
        if cell_value in a[num_of]:
            a[num_of].remove(cell_value)
            k -= 1
    except TypeError:
        sys.stdout.write(".")
    return k
