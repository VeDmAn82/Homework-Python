# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N  (60 -> 2, 2, 3, 5)

n = int(input('Введите натуральное число N: '))
list = []
i = 2
while (n != 1):
    if n % i == 0:
        list.append(i)
        n = n / i
        i = 2
    else:
        i += 1
print(f'Простые множители числа N: {list}')
 