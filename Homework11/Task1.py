# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно

import matplotlib.pyplot as plt

def FunctionGraph():
    x = [x for x in range(-10, 11)]
    y = [5 * i**2 + 10 * i - 30 for i in x ]
    listX = []
    listY = []
    for i in range(len(y)):
        if y[i] < 0:
            listX.append(x[i])
            listY.append(y[i])  
    plt.plot(x, y)
    plt.plot(listX, listY)           
    plt.title("Line graph")   
    plt.ylabel('Y axis')   
    plt.xlabel('X axis')   
    plt.show()

FunctionGraph()

