import sys
import subprocess
from datetime import datetime
import copy

import time
from operator import itemgetter


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
            if i!=80:
                sys.stdout.write("| ")
    return


def tabulated_change(list_):
    # Вывод на экран
    k = 8
    for j in range(0, 64):
        sys.stdout.write("-")
    sys.stdout.write("\n")
    sys.stdout.write("| ")
    for i in range(0, 81):
        b = str(i + 1) + ":" + "{:^1}".format(str(list_[i])) + " "
        a = str(i + 1) + ":" + "{:^1}".format(str(list_[i]))
        if i < 9:
            sys.stdout.write(b)
        else:
            sys.stdout.write(a)
        sys.stdout.write(" | ")
        if i // k == 1:
            k += 9
            sys.stdout.write("\n")

            for j in range(0, 64):
                sys.stdout.write("-")
            sys.stdout.write("\n")
            sys.stdout.write("| ")
    return

# Доработать
def sudoku_file(list_, key):
    f = open("sudoku_answer.txt", 'a+')
    f.write(str(datetime.now()) + '\n')
    if key == 'answer':
        f.write("Решение:")
    if key == 'sudoku':
        f.write("Ваше судоку:")
    f.write("\n")
    k = 8
    for j in range(0, 37):
        f.write("-")
    f.write("\n")
    f.write("| ")
    for i in range(0, 81):
        a = "{:^1}".format(str(list_[i]))
        f.write(a)
        f.write(" | ")
        if i // k == 1:
            k += 9
            f.write("\n")

            for j in range(0, 37):
                f.write("-")
            f.write("\n")
            if i != 80:
                f.write("| ")
    if key == 'answer':
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    f.close()


def printello(list_):
    list_auto = [0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 2, 0, 7, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 5, 0, 0, 0,
                 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 6, 1, 0, 2, 8, 0, 0, 0, 9, 0, 0, 0, 0, 2, 4, 6, 0,
                 0, 0, 0, 8, 3, 0, 0, 0, 7, 0, 0, 0, 0, 0, 9]

    def HELP():
        print("Для изменения элемента введите команду CHANGE")
        print("Для полного ввода заново введите AGAIN")
        print("Для вызова базы данных по предыдущим играм введите SHOWBD")
        list_[i] = input(f"Введите команду\n  или  \n{i + 1} элемент = ")

    def CHANGE():

        subprocess.Popen("cls",
                         shell=True).communicate()
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
    i = 0
    while i != 81:

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
            if list_[i] == 'KEK':
                list_=list_auto
                i = 80
                break
            if list_[i] == 'CHANGE' or list_[i] == 'change':
                list_[i] = ' '
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
        i += 1
    sudoku_file(list_, 'sudoku')
    CHECK()
    return list_
