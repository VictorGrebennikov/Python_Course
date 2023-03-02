# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько
# легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

all_vowels = "аеиоуыэюя"
vowels_count = []

inp_word = input("Enter text: ").split()

for chars in inp_word:
    char_spl = list(chars)
    vowel_in_word = sum([1 for i in char_spl if i in all_vowels])
    vowels_count.append(vowel_in_word)

if len(list(set(vowels_count))) < 2 and list(set(vowels_count))[0] != 0:
    print("Парам пам-пам")
else:
    print("Пам парам")