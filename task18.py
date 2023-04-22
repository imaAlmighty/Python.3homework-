# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X . Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
n = int(input('Enter length of array: '))
array = [randint(1, 100) for i in range(n)]
print(array)

x = int(input('Enter number: '))
min_number = array[0]
for i in array:
    current_difference = abs(i-x)
    if current_difference < min_number:
        result = i
        min_number = current_difference
result = min([i for i in array if abs(i-x) == min_number])
print(f'Result = {result}')
