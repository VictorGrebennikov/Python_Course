# Фибоначчи
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def sequence(num):
    if num in [0, 1]:
        return 1
    return sequence(num - 1) + sequence(num - 2)

print(sequence(int(input("Enter number: "))))