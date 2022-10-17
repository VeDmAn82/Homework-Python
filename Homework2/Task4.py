# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо

N = int(input('Enter number N: '))
n = int(input('Enter shift number: '))

list = []
for i in range(-N, N+1):
    list.append(i)       
print(list)

def right_shift(list, n):
    a = n % len(list)
    return list[-a:] + list[:-a]

list = right_shift(list, n)
print(list)
