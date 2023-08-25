# Co zrobimy / Co chcemy uzyskać
# 1 - dodawać elementy do listy
# 2 - usuwać elementy ze listy
# 3 - edytować elementy w listy
# 4 - wyświetlać elementy w liście wraz z indeksami

my_list = []

while True:
    command = input("Podaj komendę: \n")

    if command == "dodaj":
        value = input("Podaj nową wartość w liście: \n")
        my_list.append(value)

    elif command == "usuń":
        value = input("Podaj wartość do usunięcia: \n")
        if value in my_list:
            my_list.remove(value)
        else:
            print("Nie ma takiej wartości w liście. \n")

    elif command == "edytuj":
        index = int(input("Podaj index: \n"))
        if len(my_list) - 1 >= index:
            value = input("Podaj wartość do nadpisania: \n")
            my_list[index] = value
        else:
            print("Nie ma takiego indeksu w liście. \nPodaj inny index: \n")
            continue    # Możesz pokombinować żeby zaczynało się od tego samego miejsca, a nie od dodawania komendy.

    elif command == "wyświetl":
        for index, value in enumerate(my_list):
            print(f"{index}. {value} \n")

    elif command == "exit":
        break

    else:
        print("Nie ma takiej komendy. \n")
