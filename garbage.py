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
from base_sudoku import *

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