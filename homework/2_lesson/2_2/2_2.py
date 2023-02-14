# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os

os.system('cls')

n = int(input("Enter number: "))
degree_of_two = 0
number = 0

while number < n:
    number = 2**degree_of_two
    if number < n:
        print(number)
        degree_of_two += 1
