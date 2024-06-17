from data_create import *
from highlight_data import *


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if var == 1:
        with open('data_1.csv', 'a', encoding= 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_2.csv', 'a', encoding= 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print("Вывожу данные из 1-го файла: \n")
    with open('data_1.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append((''.join(data_first[j:i+1])))
                j = i
        print(''.join(data_first_list))

    print("Вывожу данные из 2-го файла: \n")
    with open('data_2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def change_data():
    print(print_data())
    print("Выберете словарь, в котором нужно заменить данные: 1 или 2 ")
    command = int(input())
    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if command == 1:
        print("Выберете фамилию, для которой Вы хотите изменить данные: ")
        x = input()
        index = insert_1(x)
        if index == "Такой фамилии в справочнике нет.":
            print("Такой фамилии в справочнике нет.")
            return

        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        new_data_first = []
        with open('data_1.csv', 'r') as f:
            old_data_first = f.readlines()
            new_data_first.append(old_data_first[0:index-1])
            new_data_first.append(name + '\n')
            new_data_first.append(surname + '\n')
            new_data_first.append(phone + '\n')
            new_data_first.append(address + '\n')
            new_data_first.append(old_data_first[index + 3:-1])

        with open('data_1.csv', 'w+') as f:
            for line in new_data_first:
                f.writelines(line)

    if command == 2:
        print("Выберете фамилию, для которой Вы хотите изменить данные: ")
        x = input()
        index = insert_2(x)
        if index == "Такой фамилии в справочнике нет.":
            print("Такой фамилии в справочнике нет.")
            return
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        new_data_second = []
        with open('data_2.csv', 'r') as f:
            old_data_second = f.readlines()
            new_data_second.append(old_data_second[0: index])
            new_data_second.append(f"{name};{surname};{phone};{address}\n")
            new_data_second.append(old_data_second[index + 1:])
        with open('data_2.csv', 'w+') as f:
            for line in new_data_second:
                f.writelines(line)


def delit_data():
    print(print_data())
    print("Выберете словарь, в котором нужно заменить данные: 1 или 2 ")
    command = int(input())
    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if command == 1:
        print("Выберете фамилию, для которой Вы хотите удалить данные: ")
        x = input()
        index = insert_1(x)
        if index == "Такой фамилии в справочнике нет.":
            print("Такой фамилии в справочнике нет.")
            return
        new_data_first = []
        with open('data_1.csv', 'r') as f:
            old_data_first = f.readlines()
            new_data_first.append(old_data_first[0:index-1])

            new_data_first.append(old_data_first[index + 3:-1])

        with open('data_1.csv', 'w+') as f:
            for line in new_data_first:
                f.writelines(line)

    if command == 2:
        print("Выберете фамилию, для которой Вы хотите удалить данные: ")
        x = input()
        index = insert_2(x)
        if index == "Такой фамилии в справочнике нет.":
            print("Такой фамилии в справочнике нет.")
            return
        new_data_second = []
        with open('data_2.csv', 'r') as f:
            old_data_second = f.readlines()
            new_data_second.append(old_data_second[0: index-1])
            new_data_second.append(old_data_second[index + 1:-1])
        with open('data_2.csv', 'w+') as f:
            for line in new_data_second:
                f.writelines(line)


