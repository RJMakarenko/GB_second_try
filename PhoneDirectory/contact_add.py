import os
from pause import pause


def contact_add():
    os.system('cls')
    print('Добавление контакта:\n')
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    with open('phones.txt', encoding='utf-8') as file:
        data = file.readlines()
    with open('phones.txt', encoding='utf-8', mode='a') as file:
        file.write(f'\n{surname.capitalize()} {name.capitalize()} {phone}')
    print('Контакт успешно добавлен!')
    pause()


