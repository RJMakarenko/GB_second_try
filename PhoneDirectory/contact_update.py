import os
from pause import pause
from take_contacts import take_contacts
from contact_search import search


def contact_update():
    os.system('cls')
    print('Изменение контакта')
    print()
    surname_for_delete = input('Введите фамилию: ').capitalize()
    data = take_contacts()
    search_result = search(surname_for_delete, search_type='Фамилия')
    print('\nРезультаты поиска: \n')
    if 'Контакт не найден' in search_result[-1]:
        print('Контакт не найден')
    else:
        to_update = []
        for number, item in enumerate(search_result[1:]):
            print(f'{number + 1}. {item}')
            to_update.append(item)
        update_number = int(input('\nВведите номер контакта для изменения: '))
        print()
        print('''Изменение контакта: 

            1. Изменить фамилию
            2. Изменить имя
            3. Изменить номер телефона
            4. Отмена

            ''')
        update_type = int(input('Выберите действие: '))
        old_surname, old_name, old_phone = to_update[update_number - 1].split()
        if update_type == 1:
            new_surname = input('Введите фамилию: ')
            to_update[update_number - 1] = f'{new_surname} {old_name} {old_phone}'
        elif update_type == 2:
            new_name = input('Введите имя: ')
            to_update[update_number - 1] = f'{old_surname} {new_name} {old_phone}'
        elif update_type == 3:
            new_phone = input('Введите номер телефона: ')
            to_update[update_number - 1] = f'{old_surname} {old_name} {new_phone}'
        else:
            return
        print()
        for key, value in data.items():
            if value['Фамилия'] == old_surname and value['Имя'] == old_name:
                data[key]['Фамилия'], \
                    data[key]['Имя'], \
                    data[key]['Номер телефона'] = to_update[update_number - 1].split()
        with open('phones.txt', encoding='utf-8', mode='w') as file:
            for person in data.values():
                file.write(f'\n{person["Фамилия"]} {person["Имя"]} {person["Номер телефона"]}')
        print('Данные успешно изменены!')
        pause()
