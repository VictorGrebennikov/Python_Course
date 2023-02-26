# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Пример:
# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

nums = [int(i) for i in input("Enter a list of numbers: ").split()]
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

print([ind for ind, i in enumerate(nums) if lower_limit < i < upper_limit])
