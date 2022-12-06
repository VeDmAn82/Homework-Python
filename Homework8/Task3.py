# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

import random
from datetime import datetime, timedelta

def MinMaxAverageTemp():
    temperature = [0] * 5
    result = []
    weekMax = 0
    weekMin = 250
    temperature[0] = list(random.randint(8, 18) for i in range(31))
    temperature[1] = list(random.randint(12, 25) for i in range(30))
    temperature[2] = list(random.randint(15, 30) for i in range(31))
    temperature[3] = list(random.randint(14, 27) for i in range(31))
    temperature[4] = list(random.randint(6, 17) for i in range(30))
    for row in temperature:
        print(row)
    for i in range(len(temperature)):
        for j in range(len(temperature[i])):
            result.append(temperature[i][j])
    for i in range(len(result) - 6):
        resultSum = 0
        resultSum = sum(result[i:i+6]) 
        if resultSum > weekMax:
            weekMax = i
        elif resultSum < weekMin:
            weekMin = i
    startDate = '01-05-2022' 
    dt = datetime.strptime(startDate, '%d-%m-%Y')
    resultStartMaxDay = (dt + timedelta(days = weekMax)).strftime('%d-%m-%Y')
    resultFinishMaxDay = (dt + timedelta(days = weekMax + 7)).strftime('%d-%m-%Y')
    resultStartMinDay = (dt + timedelta(days = weekMin)).strftime('%d-%m-%Y')
    resultFinishMinDay = (dt + timedelta(days = weekMin + 7)).strftime('%d-%m-%Y')
    print(f"Самая теплая неделя начивается с {resultStartMaxDay} по {resultFinishMaxDay}")
    print(f"Самая холодная неделя начивается с {resultStartMinDay} по {resultFinishMinDay}")

MinMaxAverageTemp()