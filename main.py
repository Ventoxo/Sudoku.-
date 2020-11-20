from base_sudoku_9 import *
import copy
from text_sudoku import *
import time




# Разработчик: Дьяков Никита
# @Ventoxo - telegram
# Start_date 06.11.2020
# End_date   20.11.2020
exit_name = 'y'
while exit_name == 'Y' or exit_name == 'y':
    sudoku_9 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    sudoku_9=printello(sudoku_9)

    k = fill_empty_cell_9(sudoku_9)

    temp_k = 0
    kit = 1
    start_time = time.time()
    while k != 0:

        if temp_k == k:

            k = abstraction(sudoku_9, k, search_list_element(sudoku_9, 0))
        if kit == 1:
            temp_k = k
        kit *= -1
        k = hard_complicated(sudoku_9, k)

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Судоку решено")


    print("Ваше судоку и ответ на него вы можете найти в файле sudoku_answer.txt")
    print("Если Вам надо решить еще одно судоку, введите y или Y")
    exit_name = input("Y or any_key? ")
exit()


