import os
from pause import pause
from take_contacts import take_contacts


def search(element, search_type=None):
    data = take_contacts()
    result = ['Результаты поиска:\n']
    for item in data.values():
        if element in item.get(search_type):
            result.append(f'{item["Фамилия"]} {item["Имя"]}'
                          f'{" " * (25 - (len(item["Фамилия"]) + len(item["Имя"])))}'
                          f'{item["Номер телефона"]}')
    if len(result) == 1:
        result.append('Контакт не найден\n')
    return result


def contact_search():
    os.system('cls')
    print()
    print('''Поиск контакта: 
    
    1. По фамилии
    2. По имени
    3. По номеру телефона
    4. Отмена
    
    ''')
    print()
    search_type = int(input('Выберите действие: '))
    if search_type == 1:
        surname = input('Введите фамилию: ').capitalize()
        print(*search(surname, search_type='Фамилия'), sep='\n')
        print()
        pause()
    elif search_type == 2:
        name = input('Введите имя: ').capitalize()
        print(*search(name, search_type='Имя'), sep='\n')
        print()
        pause()
    if search_type == 3:
        phone = input('Введите номер телефона: ')
        print(*search(phone, search_type='Номер телефона'), sep='\n')
        print()
        pause()
    else:
        return

