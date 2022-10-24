# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

path = 'icecream.txt'
data = open(path, 'r', encoding='utf-8')
assortment = list(data.readline().rstrip().split(', '))
balance = list(data.readline().rstrip().split(', '))
data.close()
list = []
for element in assortment:
    if element not in balance:
        list.append(element)
print(assortment)
print(balance)
print(f'Закончилось:', *list)
