def take_contacts():
    with open('phones.txt', encoding='utf-8') as file:
        data = sorted(file.readlines())
    data_to_view = {}
    number = 1
    for person in data:
        if len(person) != 1:
            second_name, first_name, phone = person.split()
            data_to_view[number] = {'Фамилия': second_name, 'Имя': first_name, 'Номер телефона': phone}
            number += 1
    return data_to_view

