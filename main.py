# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
print(f'Задача 1')
from math import *
d = int(input('Введите число: '))
print(f'Число "пи" с заданной точностью {d} равно {round(pi, d)}')


# 2 Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
print(f'Задача 2')
def prime_factors(n):
    i = 2
    lst_prime = []
    while i * i <= n:
        while n % i == 0:
            lst_prime.append(i)
            n/=i
        i += 1
    if n > 1:
        lst_prime.append(int(n))
    return lst_prime
n = int(input('Введите число: '))
print(prime_factors(n))

# 3 Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

print(f'Задача 3')
import random

list1 = []

for i in range(10):
    list1.append(random.randint(1, 10))
print(f'Исходный список: {list1}')

list2 = []
count = 0
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(f'Список неповторяющихся элементов: {list2}')