from logger import *


def interfase():
    print("Вы попали на справочник! \n 1 - запись данных \n 2 - вывод данных \n 3 - изменить данные \n 4 - удалить данные")
    command = int(input("Введите число "))

    while command < 1 or command > 4 :
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delit_data()