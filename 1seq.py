'''
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
'''

number_elements_list = int(input('Введите количество элементов: '))
num_list = []
for element_list in range(number_elements_list):
    num = int(input(f'Введите {element_list + 1} элемент: '))
    num_list.append(num)
num_list.sort()
print('Вывод:',num_list)

