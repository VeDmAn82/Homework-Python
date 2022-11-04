# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

numbers = [random.randint(1, 10) for i in range(8)]
print(numbers)

list_origin = []
[list_origin.append(i) for i in numbers if i not in list_origin]
print(f'Список уникальных элементов {list_origin}')

