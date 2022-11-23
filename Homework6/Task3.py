# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11

from fractions import Fraction
denominator = 11
result = set()
for i in range(1, denominator):
    for j in range(1, denominator + 1):
        if i < j and i//j != i/j and (n := Fraction(i,j)) not in result:
            print(n)
            result.add(n)