'''
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''

