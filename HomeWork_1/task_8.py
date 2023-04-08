n = int(input('Введите сторону n: '))
m = int(input('Введите сторону m: '))
k = int(input('Введите число k: '))
if (k % m == 0 or k % n == 0) and  k < n * m :
    print('У вас все получится!')
elif k == n * m:
    print('Жадина! Забирайте целиком!')
else:
    print('К сожалению, не выйдет!')
