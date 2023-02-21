# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Size of the first set: "))
m = int(input("Size of the second set: "))

set_1 = [int(input("Enter number for set_1: ")) for i in range(n)]
set_2 = [int(input("Enter number for set_2: ")) for i in range(m)]

print(sorted(set(set_1).intersection(set_2)))