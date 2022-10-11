# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

d = float(
    input("Введите количество чисел по шаблону в пределах от 0.1 до 0.0000000001: "))

count = 0
while d < 1:
    d = d * 10
    count = count + 1

print("{:.{}f}".format(pi, count))


# from decimal import Decimal


# def calculattion_number (number, d):
#     num1 = Decimal(number)
#     num1 = num1.quantize(Decimal(d))
#     return num1


# number = input ('Enter a real number:  ')
# d = input (' Enter the required accuracy d:  ')
# print(calculattion_number (number, d))
