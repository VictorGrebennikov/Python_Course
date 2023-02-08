# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# in
# 3 2 4
# out
# yes

# in
# 3 2 1
# out
# no

n = int(input("Enter 'n' slices: "))
m = int(input("Enter 'm' slices: "))
k = int(input("Enter 'k' slices: "))

if k >= n or k >= m:
    a = 0
    count = 1
    while k > a and m > count:
        a = n * count
        count += 1
        if a == k:
            print("yes")
            exit()

    a = 0
    count = 1
    while k > a and n > count:
        a = m * count
        count += 1
        if a == k:
            print("yes")
            exit()
    print("no")
else:
    print("no")
