# чисто мусор из других файлов
sudoku = {}
f = open('text.txt')
sudoku = f.read().splitlines()

print(sudoku)
data = []

with open("text.txt") as f:
    for char in f.read():
        process(char)
    for line in f:
        data.append([int(x) for x in line.split()])
print(data)
data = list(data)
print(data)
print(data[2])
print(process[3])

def delete_problem(a):
    k = {}
    j = 0
    for i in a:
        if i != ' ':
            k[j] = i
            j += 1
    return k

def fish(a):
    a[2], a[3] = a[4], a[5]
    a[10], a[11] = a[12], a[13]

)
from base_sudoku_9 import *

#sudoku = [1, 2, 3, 4, 4, 0, 2, 1, 0, 1, 4, 3, 3, 4, 1, 2]
sudoku_9 = [4, 0, 0, 1, 9, 8, 6, 5, 0, 0, 5, 9, 0, 0, 0, 2, 1, 4, 1, 0, 3, 0, 5, 0, 0, 9, 0, 0, 1, 8, 7, 0, 5, 9, 0, 6,
            0, 7, 0, 6, 1, 0, 3, 4, 0, 9, 4, 6, 2, 0, 0, 0, 7, 5, 7, 0, 2, 9, 3, 4, 0, 0, 1, 0, 9, 0, 8, 0, 7, 0, 3, 2,
            6, 0, 4, 0, 0, 1, 7, 0, 9]

'''for i in range(0, 81):
    sudoku_9.append(int(input()))
print(sudoku_9)'''

#k = fill_empty_cell_4(sudoku)
k = fill_empty_cell_9(sudoku_9)

for i in range(0, 81):
    print(f"{i}={sudoku_9[i]}")
print(len(sudoku_9))
print(sudoku_9)
temp_k = 0
print(sudoku_9[19])
kit=1
while k != 0:
    print(k)
    '''for i in range(0, 16):
        k = check_columns_4(sudoku, i, k)
        k = check_str_4(sudoku, i, k)'''
    if temp_k == k:
        break
    if kit==1:
        temp_k = k
    kit*=-1
    for i in range(0, 81):
        '''print(i)'''
        if type(sudoku_9)==type(sudoku_9[i]):
            #print(type(sudoku_9), type(sudoku_9[i]))
            k = check_columns_9(sudoku_9, i, k)
            k = check_str_9(sudoku_9, i, k)

print("")
print(sudoku_9)


def abstraction(a: "сам массив", k: "счетчик основного цикла", i: "номер элемента для абстракции"):
    # на случай, если нет решения, например, для сложных судоку
    temp_k = 0
    kit = 1
    empty_holder = []
    temp_a = []

    b = copy.deepcopy(a)
    temp_a = b[i]
    try:
        b[i] = b[i][0]
    except IndexError:
        obnul(b[i])
    temp_kk = k

    while k != 0:
        temp_kk = hard_complicated(b, k)
        if empty_holder in b:
            try:
                a[i].pop(0)
            except IndexError:
                break
            b = copy.deepcopy(a)
            temp_a = b[i]
            temp_kk = k - 1

        if temp_k == k:
            print(k)
            print(temp_kk)
            tabulated(a)
            #k = abstraction(b, k, search_list_element(b, i + 1))
        if kit == 1:
            temp_k = k
        kit *= -1
    tabulated(a)
    a = b
    a[i] = obnul(a[i])
    return temp_kk


Поиск самого меньшего повторения в квадрате, абстракция по нему

def abstraction(a: "сам массив", k: "счетчик основного цикла", i: "номер элемента для абстракции"):
    # на случай, если нет решения, например, для сложных судоку
    if i=="Valet":
        tabulated(a)
        exit()

    temp_k = 0
    kit = 1
    empty_holder = []

    b = copy.deepcopy(a)
    k -= len(b[i])+1
    b[i] = b[i][0]
    temp_kk = k

    while temp_kk != 0:
        temp_kk = hard_complicated(b, temp_kk)
        if empty_holder in b:
            try:
                a[i].pop(0)

            except IndexError:
                return k
            b = copy.deepcopy(a)
            obnul(b[i])
            if isinstance(b[i],list):
                b[i] = b[i][0]
            temp_kk = temp_kk - 1

        if temp_k == temp_kk:
            #print(k)
            #print(temp_kk)
            tabulated(b)
            temp_kk = abstraction(b, k, search_list_element(b, i + 1))
        if kit == 1:
            temp_k = temp_kk
        kit *= -1
    #tabulated(a)
    return temp_kk