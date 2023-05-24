import os
from pause import pause
from take_contacts import take_contacts
from contact_search import search


def contact_delete():
    os.system('cls')
    print('Удаление контакта')
    print()
    surname_for_delete = input('Введите фамилию: ').capitalize()
    data = take_contacts()
    search_result = search(surname_for_delete, search_type='Фамилия')
    print('\nРезультаты поиска: \n')
    if 'Контакт не найден' in search_result[-1]:
        print('Контакт не найден')
    else:
        to_delete = []
        for number, item in enumerate(search_result[1:]):
            print(f'{number + 1}. {item}')
            to_delete.append(item)
        delete_type = input('\nВведите номер контакта для удаления или '
                            '"Все" для удаления всех найденных: ').capitalize()
        if delete_type == 'Все':
            old_data = data.copy()
            for item in to_delete:
                surname, name, phone = item.split()
                for key, value in old_data.items():
                    if value['Фамилия'] == surname and value['Имя'] == name:
                        data.pop(key)
        else:
            old_data = data.copy()
            surname, name, phone = to_delete[int(delete_type) - 1].split()
            for key, value in old_data.items():
                if value['Фамилия'] == surname and value['Имя'] == name:
                    data.pop(key)
        with open('phones.txt', encoding='utf-8', mode='w') as file:
            for person in data.values():
                file.write(f'\n{person["Фамилия"]} {person["Имя"]} {person["Номер телефона"]}')
        print('Данные успешно удалены!')
    print()
    pause()
