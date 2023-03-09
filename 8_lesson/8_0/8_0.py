from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        id = int(all_data[-1][0])
        return all_data


def show_all():
    print(*all_data, sep="\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                play = False
            case _:
                print("Try again!\n")


main_menu()