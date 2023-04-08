n = int(input('Введите трехзначное число: '))
if len(str(n)) != 3:
    print('Вы ввели не трехзначное число!!!')
else:
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    print(f'Сумма цифр введённого числа равна {sum_of_digits}')
