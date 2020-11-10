from base_sudoku import *

# sudoku = [1, 2, 3, 4, 4, 0, 2, 1, 0, 1, 4, 3, 3, 4, 1, 2]
'''sudoku_9 = [4, 0, 0, 1, 9, 8, 6, 5, 0, 0, 5, 9, 0, 0, 0, 2, 1, 4, 1, 0, 3, 0, 5, 0, 0, 9, 0, 0, 1, 8, 7, 0, 5, 9, 0, 6,
            0, 7, 0, 6, 1, 0, 3, 4, 0, 9, 4, 6, 2, 0, 0, 0, 7, 5, 7, 0, 2, 9, 3, 4, 0, 0, 1, 0, 9, 0, 8, 0, 7, 0, 3, 2,
            6, 0, 4, 0, 0, 1, 7, 0, 9]'''

sudoku_9 = [0, 9, 0, 5, 0, 8, 0, 0, 0, 2, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 8, 4, 0, 0, 7, 0, 1, 6, 0, 0, 0,
            0, 0, 0, 0, 9, 0, 4, 0, 1, 1, 0, 4, 0, 0, 2, 0, 9, 0, 0, 0, 0, 0, 8, 0, 5, 7, 2, 0, 2, 5, 6, 0, 0, 0, 4, 0,
            7, 1, 0, 2, 4, 0, 0, 0, 0]
'''for i in range(0, 81):
    sudoku_9.append(int(input()))
f = open("Sudoku_logs.txt", "w")
f.write(str(sudoku_9))
f.close()'''
# k = fill_empty_cell_4(sudoku)
k = fill_empty_cell_9(sudoku_9)

for i in range(0, 81):
    print(f"{i}={sudoku_9[i]}")

temp_k = 0
kit = 1
while k != 0:
    print(f"k={k}")
    '''for i in range(0, 16):
        k = check_columns_4(sudoku, i, k)
        k = check_str_4(sudoku, i, k)'''
    if temp_k == k:
        break
    if kit == 1:
        temp_k = k
    kit *= -1
    for i in range(0, 81):
        '''print(i)'''
        if type(sudoku_9) == type(sudoku_9[i]):
            k = check_columns_9(sudoku_9, i, k)
            k = check_str_9(sudoku_9, i, k)
            k = check_yadro_9(sudoku_9, i, k)

        try:
            if len(sudoku_9[i]) == 1:
                sudoku_9[i] = sudoku_9[i].pop()
        except TypeError:
            sys.stdout.write(".")

k = 8
for j in range(0, 206):
    sys.stdout.write("-")
sys.stdout.write("\n")
for i in range(0, 81):
    a = "{:^15}".format(str(sudoku_9[i]))
    sys.stdout.write(a)
    sys.stdout.write(" | ")
    if i // k == 1:
        k += 9
        sys.stdout.write("\n")
        for j in range(0, 206):
            sys.stdout.write("-")
        sys.stdout.write("\n")
print("")
print(sudoku_9)
