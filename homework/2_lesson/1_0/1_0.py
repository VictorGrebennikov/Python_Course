# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import os

os.system('cls')

n = int(input("Enter number of coins: "))
count = 0

for i in range(n):
    temp = int(input("Enter 0 ог 1: "))
    if temp == 0:
        count += 1
        temp = 0

if n - count < n / 2:
    print(n - count)
else:
    print(count)
