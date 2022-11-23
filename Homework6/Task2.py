# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом. [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да  [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

size = 15
numbers = [random.randint(0, 9) for i in range(size)]
print(numbers)

findNumber = list(map(int, input('Введите трехзначное число: ')))

for i in range(len(numbers)):
    if numbers[i:i+3] == findNumber:
        print('Да')
        break
else:
    print('Нет')



