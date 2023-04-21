scrabble_dict = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10,
                 'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}
string = input('Введите слово: ')
cnt = 0
for letter in string:
    for key in scrabble_dict.keys():
        if letter.upper() in key:
            cnt += scrabble_dict[key]
print(f'Слово "{string.title()}" это {cnt} очков в Scrabble!')


