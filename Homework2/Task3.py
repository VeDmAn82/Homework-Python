# Задача 3. Даны две строки: «one» «onetwonine».
# Посчитайте сколько раз каждый символ первой строки встречается во второй

string_1 = 'one'
string_2 = 'onetwonine'
for i in range(len(string_1)):
    count = 0
    for j in range(len(string_2)):
        if string_1[i] == string_2[j]:
            count += 1
    print(f'{string_1[i]} - {count} раз(а)')
 
