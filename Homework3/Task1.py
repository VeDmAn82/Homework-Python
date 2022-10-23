# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи. 6 –> 1 1 2 3 5 8

def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

num = int(input('Введите количество элементов N: ' ))
data = open('fibonacci.txt', 'w')
for i in range(1, num+1):
    result = fib(i)
    print(result, end=' ')
    data.writelines(str(result) + '\n')
data.close()
