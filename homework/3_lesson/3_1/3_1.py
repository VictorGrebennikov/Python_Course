# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

numbers_of_items = int(input("Enter the number of items: "))
list_of_items = [i for i in range(1, numbers_of_items + 1)]
print(list_of_items)

x_number = int(input("Enter X-number: "))

if numbers_of_items < x_number:
    print(numbers_of_items)
else:
    print(x_number-1)