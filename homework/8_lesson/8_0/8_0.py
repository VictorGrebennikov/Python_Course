from os import path
import os

os.system('cls')


file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])

        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ["surname", "", "surname_2", "phone_number"]
    string = ""
    for i in array:
        string += input(f"enter {i} ") + " "
    id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{id} {string}\n")


def search_contact():
    search_data = input("Enter the search data: ")
    search = [i for i in all_data if search_data in i]
    if search:
        print(*search, sep="\n")
    else:
        print("The data is not exists")


def delete_contact():
    global all_data, id
    show_all()
    del_item = input("Enter number for delete: ")

    all_data = [i for i in all_data if i[0] != del_item]

    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data) + "\n")


def export_bd():
    new_name_bd = input("Enter a new file name to save: ")
    if not path.exists(new_name_bd):
        with open(f"{new_name_bd}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(all_data) + "\n")


def import_bd():
    global file_base
    new_base = input("Enter a file name to connect the new database: ")
    if path.exists(new_base):
        file_base = new_base
        read_records()


def change_menu():
    show_all()
    id_change = input("Enter id for change: ")
    while True:
        print("\nChanging:")
        change = input("1. surname\n"
                       "2. name\n"
                       "3. patronymic\n"
                       "4. phone number\n"
                       "5. exit\n")

        match change:
            case "1" | "2" | "3" | "4":
                data_change = input("Enter change data: ")
                return id_change, change, data_change
            case "5":
                return 0
            case _:
                print("Incorrect input. Try again.")


def change_contact(active):
    global all_data
    id_change, change, data_change = active

    for i, j in enumerate(all_data):
        if j[0] == id_change:

            j = j.split()
            j[int(change)] = data_change
            all_data[i] = " ".join(j)

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write("\n".join(all_data) + "\n")
    print("Record changed!\n")
    show_all()


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone base:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete\n"
                       "5. Export\n"
                       "6. Import\n"
                       "7. Change\n"
                       "8. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                delete_contact()
            case "5":
                export_bd()
            case "6":
                import_bd()
            case "7":
                active = change_menu()
                if active:
                    change_contact(active)
            case "8":
                play = False
            case _:
                print("Try again!\n")


main_menu()
