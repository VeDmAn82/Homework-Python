# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы

import random

def Function():
    rows = 4
    columns = 4
    numbers = [0] * rows
    sumMainDiagonal = 0
    for i in range(len(numbers)):
        numbers[i] = list(random.randint(0, 9) for _ in range(columns))
    for i in range(rows):
        sumMainDiagonal = sumMainDiagonal + numbers[i][i]
    for row in numbers:
        print(row)
    print(f'Сумма главной диагонали - {sumMainDiagonal}')

    resultSum = []
    for row in numbers:
        sumRow = 0
        for i in range(len(row)):
            sumRow = sumRow + row[i]
        resultSum.append(sumRow)
    
    resultSumRow = 0
    index = 0
    for i in range(len(resultSum)):
        if resultSum[i] > sumMainDiagonal:
            resultSumRow = resultSum[i]
            index = resultSum.index(resultSum[i]) + 1
            print(f"Сумма строки {index} превосходит сумму главной диагонали и равна {resultSumRow}")
            break
    else:
        print("Нет строки, превосходящей сумму главной диагонали")
     
Function()   
