# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN (N может быть любой длины)
# N = 132: 132 + 132132 + 132132132 = 132264396

number = int(input('Введите число: '))
result = number + int(str(number)*2) + int(str(number)*3)
print(result)