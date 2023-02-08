# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# in
# 385916

# out
# yes

num = int(input("Enter six digit number: "))

n = 100000
right_sum = left_sum = 0

if num > 1000000 or num < 100000:
    print("The number is not six digit!")
    exit()
else:
    while n > 1:
        right_sum = right_sum + (num//n % 10)
        left_sum = left_sum + (num % 10)
        num //= 10
        n //= 100

if right_sum == left_sum:
    print("yes")
else:
    print("no")
