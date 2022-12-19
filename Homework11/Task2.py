# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов,
# отсортированных по площади. Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, 
# цены от 3 до 20 млн

from matplotlib import pyplot as plt  
from random import randint as rand

def HouseData():
    number_houses = [i for i in range(1, 16)]
    square_houses = [rand(100, 300) for i in range(len(number_houses))]
    prices_houses = [rand(3000000, 20000000) for i in range(len(number_houses))]
    required_price = 50000
    required_price_line = [required_price for i in range(len(number_houses))]
    prices_meter = [int(prices_houses[i]/square_houses[i]) for i in range(len(number_houses))]
    
    plt.bar(number_houses, prices_meter)
    plt.plot(number_houses, required_price_line, 'r')
    plt.title("Стоимость домов за кв. метр")   
    plt.ylabel('Стоимость')   
    plt.xlabel('№ дома') 
    plt.show()

    result_number_houses = []
    result_square_houses = []
    result_prices_houses = []
    result_prices_meter = []

    for i in range(len(number_houses)):
        if prices_meter[i] < required_price:
            result_number_houses.append(number_houses[i])
            result_square_houses.append(square_houses[i])
            result_prices_houses.append(prices_houses[i])
            result_prices_meter.append(prices_meter[i])
    
    for i in range(len(result_square_houses)-1):
        for j in range(len(result_square_houses)-i-1):
            if result_square_houses[j] > result_square_houses[j + 1]:
                result_square_houses[j], result_square_houses[j + 1] = result_square_houses[j + 1], result_square_houses[j]
                result_number_houses[j], result_number_houses[j + 1] = result_number_houses[j + 1], result_number_houses[j]
                result_prices_houses[j], result_prices_houses[j + 1] = result_prices_houses[j + 1], result_prices_houses[j]
                result_prices_meter[j], result_prices_meter[j + 1] = result_prices_meter[j + 1], result_prices_meter[j]

    data = open('houses.txt', 'w')
    for i in range(len(result_square_houses)):
        data.writelines(f'Number: {result_number_houses[i]} S = {result_square_houses[i]} Price: {result_prices_houses[i]} Price one meter: {result_prices_meter[i]}\n')   
    data.close

HouseData()