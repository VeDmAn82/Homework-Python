# Задача 2. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве

import math

print('Введите координаты точки А: ')
x1 = int(input())
y1 = int(input())

print('Введите координаты точки В: ')
x2 = int(input())
y2 = int(input())

def dist(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist
dist = dist(x1, y1, x2, y2)

distance = round(dist, 2)
print(distance)
