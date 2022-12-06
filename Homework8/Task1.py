# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом

import random

def BestGroupAverageScore():
    averageScoresGroups = []
    bestScore = 0
    groups = [0] * 4
    for i in range(len(groups)):
        groups[i] = list(random.randint(3, 5) for _ in range(random.randint(20, 30)))
    for score in groups:
        count = 0
        for i in range(len(score)):
            count = count + score[i]
        averageScore = count / len(score)
        averageScoresGroups.append(averageScore)
        if averageScore > bestScore:
            bestScore = round(averageScore, 2)
            bestGroup = averageScoresGroups.index(max(averageScoresGroups)) + 1
        print(score)
        print(averageScore)
    print(f'Лучший средний балл {bestScore} у группы {bestGroup}')

BestGroupAverageScore()


