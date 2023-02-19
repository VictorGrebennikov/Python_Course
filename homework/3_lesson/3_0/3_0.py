# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

numbers_of_items = int(input("Enter the number of items: "))
list_of_items = [i for i in range(1, numbers_of_items + 1)]
print(list_of_items)

x_number = int(input("Enter X-number: "))
print(len([i for i in list_of_items if i == x_number]))