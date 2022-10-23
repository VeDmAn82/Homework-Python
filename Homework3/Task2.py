# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва

data = open('fruits.txt', encoding='utf-8')
fruits = data.readlines()
data.close()
print(fruits, '\n')
letter = str(input('Введите первую букву названия фрукта: ' ))
for fruct in fruits:
    if fruct[0].lower() == letter.lower():
        print(fruct)

