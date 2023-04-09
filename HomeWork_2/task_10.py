# Вариант 1, через числа

n = int(input())
eagle = tails = 0
for i in range(n):
    coin = int(input())
    if coin == 0:
        tails += 1
    elif coin == 1:
        eagle += 1
print(min(eagle, tails))

# Вариант 2, через строки

s = input('Введите достоинства монет через пробел (0- решка, 1- орёл): ')
print(min(s.count('0'), s.count('1')))

