n = int(input('Введите количество чисел массива: '))
print('Введите значения массива: ')
arr = [int(input()) for i in range(n)]
x = int(input('Введите искомое число: '))
nearest = arr[0]
for i in range(1, len(arr)):
    if abs(arr[i] - x) < abs(nearest - x):
        nearest = arr[i]
print(f'Ближайшее число к {x} равно {nearest}.')
