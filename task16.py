# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
n = int(input('Enter length of array: '))
array = [randint(1, 100) for i in range(n)]
print(array)

number = int(input('Which number we are searching?: '))
print(f'{number} find in array {array.count(number)} times')
