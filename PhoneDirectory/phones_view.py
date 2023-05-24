import os
from pause import pause
from take_contacts import take_contacts


def phones_view():
    os.system('cls')
    data_to_view = take_contacts()
    print('\nЗаписи из телефонной книги:\n')
    if data_to_view:
        for key, person in data_to_view.items():
            print(f'{key}: {person["Фамилия"]} {person["Имя"]}'
                  f'{" " * (25 - (len(person["Фамилия"]) + len(person["Имя"])))}'
                  f'{person["Номер телефона"]}')
    else:
        print('Данных нет!')
    print()
    pause()
