n = int(input('Введите номер билетика: '))
left = sum(int(x) for x in str(n)[:3])
right = sum(int(x) for x in str(n)[3:])
if left == right:
    print('Поздравляю!! Ваш билет - счастливый!!')
else:
    print('Повезёт в следующий раз!!!')
