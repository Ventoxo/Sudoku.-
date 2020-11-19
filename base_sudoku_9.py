import copy
import sys
import subprocess
import time
from operator import itemgetter


def fill_empty_cell_9(a):
    # Заполнение пустых клеток
    cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 0
    for i in range(0, 81):
        if a[i] == 0:
            a[i] = copy.copy(cell)
            k += 9
    return k


def tabulated(list_):
    # Вывод на экран
    k = 8
    for j in range(0, 206):
        sys.stdout.write("-")
    sys.stdout.write("\n")
    for i in range(0, 81):
        a = "{:^15}".format(str(list_[i]))
        sys.stdout.write(a)
        sys.stdout.write(" | ")
        if i // k == 1:
            k += 9
            sys.stdout.write("\n")
            for j in range(0, 206):
                sys.stdout.write("-")
            sys.stdout.write("\n")
    return


def tabulated_decision(list_):
    # Вывод на экран
    k = 8
    for j in range(0, 37):
        sys.stdout.write("-")
    sys.stdout.write("\n")
    sys.stdout.write("| ")
    for i in range(0, 81):
        a = "{:^1}".format(str(list_[i]))
        sys.stdout.write(a)
        sys.stdout.write(" | ")
        if i // k == 1:
            k += 9
            sys.stdout.write("\n")

            for j in range(0, 37):
                sys.stdout.write("-")
            sys.stdout.write("\n")
            sys.stdout.write("| ")
    return


def tabulated_change(list_):
    # Вывод на экран
    k = 8
    for j in range(0, 50):
        sys.stdout.write("-")
    sys.stdout.write("\n")
    sys.stdout.write("| ")
    for i in range(0, 81):
        a = str(i + 1) + ":" + "{:^1}".format(str(list_[i]))
        sys.stdout.write(a)
        sys.stdout.write(" | ")
        if i // k == 1:
            k += 9
            sys.stdout.write("\n")

            for j in range(0, 50):
                sys.stdout.write("-")
            sys.stdout.write("\n")
            sys.stdout.write("| ")
    return


def printello(list_):
    def HELP():
        print("Для изменения элемента введите команду CHANGE")
        print("Для полного ввода заново введите AGAIN")
        print("Для вызова базы данных по предыдущим играм введите SHOWBD")
        list_[i] = input(f"Введите команду\n  или  \n{i + 1} элемент = ")

    def CHANGE():

        subprocess.Popen("cls",
                         shell=True).communicate()
        list_[i] = 0
        tabulated_change(list_)
        j = int(input('Введите номер элемента для изменения = ')) - 1
        list_[j] = int(input(f"{j + 1} элемент = "))

    # def SHOWBD():
    def CHECK():
        k = 1
        k_input = 0
        while k == 1:
            subprocess.Popen("cls",
                             shell=True).communicate()
            tabulated_decision(list_)
            if k_input == 0:
                print("Проверьте правильность ввода таблицы")
                print("Если всё введено верно введите Y, если нужно ввести корректировки - N")
            elif k_input == 1:
                print("Похоже, Вы неверно ввели значение, попробуйте снова")
            else:
                print("Если теперь всё верно - Y, если нет - N")
            key = input("Введите Y или N: ")
            if key == ("Y" or "y"):
                print("Начинаю решение")
                return
            elif key == ("N" or "n"):
                CHANGE()
                k_input = 2
            else:
                k_input = 1

        # Определение локальных ключевых переменных

    a = 0
    b_l = 0
    buffer_list = copy.deepcopy(list_)

    for i in range(0, 81):
        if b_l == 1:
            i = 0
            b_l = 2
        k = 1
        while k == 1:
            subprocess.Popen("cls",
                             shell=True).communicate()
            tabulated_decision(list_)
            print('Для помощи по командам введите HELP в поле ввода элемента')
            if a == 1 and k == 1 and b_l == 0:
                print("Вы ввели неверный элемент, попробуйте снова")
            if b_l == 2:
                print("Начинайте ввод заново")
                b_l = 0

            list_[i] = input(f"{i + 1} элемент = ")
            if list_[i] == 'HELP':
                HELP()
            if list_[i] == 'CHANGE' or list_[i] == 'change':
                CHANGE()
            elif list_[i] == 'AGAIN' or list_[i] == 'again':
                list_ = buffer_list
                b_l = 1

                break
            # elif list_[i] == ('SHOWBD' or 'showbd'):
            #   SHOWBD()
            else:
                try:
                    list_[i] = int(list_[i])
                    k = 0
                    a = 0
                except ValueError:
                    list_[i] = ' '
                    a = 1
    CHECK()


def check_str_9(a, i, k):
    # Проверка по строкам
    j = i
    for _ in range(0, 9):
        j += 1
        if j > 80:
            j -= 9
        if j // 9 == i // 9:
            k = remove_cell_value(a[j], i, a, k)
        else:
            j -= 10
    return k


def check_columns_9(a, i, k):
    # Проверка по колоннам
    j = i

    for _ in range(0, 9):
        j += 9
        if j > 80:
            j -= 81

        k = remove_cell_value(a[j], i, a, k)

    return k


def check_yadro_9(a, i, k):
    # проверка судоку по своему квадрату
    key = 0
    j = i
    for _ in range(0, 9):
        if (j + 1) // 3 == j // 3:
            j += 1
        elif (j + 7) // 27 == i // 27:
            j += 7
        else:
            j -= 20

        k = remove_cell_value(a[j], i, a, k)
    return k


def obnul(a):
    # если элемент один в массиве, массив убрать, элемент объявить обычным числом
    if len(a) == 1:
        return a.pop()
    else:
        return a


def hard_complicated(list_, k):
    # Функции собраны вместе, чтобы далее не писать каждый раз столько строк во время абстракции
    for i in range(0, 81):
        if isinstance(list_[i], list):
            k = check_columns_9(list_, i, k)
            k = check_str_9(list_, i, k)
            k = check_yadro_9(list_, i, k)
            list_[i] = obnul(list_[i])
    return k


def remove_cell_value(cell_value, num_of: int, a, k):
    # функция удаления значения из клетки

    if (cell_value in a[num_of]) and (not isinstance(cell_value, list)):
        a[num_of].remove(cell_value)
        k -= 1

    return k


def search_list_element(a, i):
    if i >= 80:
        i -= 80

    for j in range(i, 81):
        if isinstance(a[j], list):
            return int(j)
        if j == 80:
            j -= 80
    return "Valet"


empty_holder = []


def abstraction(a: "сам массив", k: "счетчик основного цикла", i: "номер элемента для абстракции"):
    # на случай, если нет решения, например, для сложных судоку
    if i == "Valet":
        tabulated_decision(a)
        exit()

    temp_k = 0
    kit = 1

    b = copy.deepcopy(a)
    k -= len(b[i]) + 1
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
            if isinstance(b[i], list):
                try:
                    b[i] = b[i][0]
                except IndexError:

                    return k
            temp_kk = temp_kk - 1

        if temp_k == temp_kk:
            # print(k)
            # print(temp_kk)
            # tabulated(b)
            temp_kk = abstraction(b, k, search_list_element(b, i + 1))
        if kit == 1:
            temp_k = temp_kk
        kit *= -1
    # tabulated(a)
    return temp_kk
