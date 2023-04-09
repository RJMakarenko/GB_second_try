sum_of_numbers = int(input('Введите сумму чисел: '))
mul_of_numbers = int(input('Введите произведение чисел: '))
for x in range(1001):
    for y in range(1001):
        if x + y == sum_of_numbers and x * y == mul_of_numbers:
            print(f'x = {x}, y = {y}')
