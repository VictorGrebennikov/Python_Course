# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6

# in
# 100
# out
# 1

three_digit_num = int(input("Enter three digit number: "))
result = 0

while three_digit_num > 0:
    result = result + int(three_digit_num % 10)
    three_digit_num = three_digit_num // 10

print(result)
