# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# По теореме Виета: x**2 + s*x + p = 0

import os

os.system('cls')

s = int(input("Enter the S-number: "))
p = int(input("Enter the P-number: "))
flag = 0
max_range = abs(p)

if abs(s) > abs(p):
    max_range = abs(s)

for i in range(-max_range, max_range + 1):
    x = i
    if (x**2 + s * x + p) == 0:
        print(x)
        flag = 1

if flag == 0:
    print("The initial numbers are incorrect!")