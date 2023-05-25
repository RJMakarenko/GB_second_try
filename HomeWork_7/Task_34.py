result = [len(list(filter(lambda x: x in 'аеёиоуыэюя', phrase))) for phrase in input().lower().split()]
print('Парам пам-пам' if all(x == result[0] for x in result) else 'Пам парам')
