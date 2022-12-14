# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности в том же порядке.
# in  7     out[4, 5, 3, 3, 4, 1, 2],  [5, 1, 2]

# in -1     out Negative value of the number of numbers!  []
# -1

# in 10     out  [4, 4, 5, 5, 6, 2, 3, 0, 9, 4], [6, 2, 3, 0, 9]

from random import randrange
from collections import Counter


def list_rand_nums(count: int):
    if count < 0:
        print("Вы ввели отрицательное число, повторите ввод")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


count = (int(input('Введите длину списка (целое положительное число): ')))
resalt = list_rand_nums(count)
tesalt_list = [len_list for len_list, v in Counter(resalt).items() if v == 1]

print(resalt)
print(tesalt_list)
