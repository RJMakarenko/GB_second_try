n = int(input('Введите количество чисел массива: '))
print('Введите значения массива: ')
arr = [input() for i in range(n)]
x = input('Введите искомое число: ')
print(f'В массиве [{", ".join(arr)}] число {x} содержится {arr.count(x)} раз.')

