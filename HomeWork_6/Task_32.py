import random

lst = [random.randint(10, 120) for x in range(10)]
print(lst)
mx = int(input('Введите максимум: '))
mn = int(input('Введите минимум: '))
indexes = [i for i in range(len(lst)) if mn <= lst[i] <= mx]
print(f'Номера индексов чисел для указанного диапазона [{mn}, {mx}]:')
print(*indexes)

