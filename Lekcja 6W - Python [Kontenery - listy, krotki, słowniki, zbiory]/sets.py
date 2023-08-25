# Co zrobimy / Co chcemy uzyskać
# 1 - dodawać elementy do zbioru
# 2 - usuwać elementy ze zbioru
# 3 - edytować elementy w zbiorze

my_set = set()  # Jedyna definicja zbioru, ponieważ poprzez x = {} definiuje się słownik

while True:
    print(my_set)
    command = input("Podaj komendę: \n")

    if command == "dodaj":
        value = input("Podaj wartość do dodania: \n")
        if value not in my_set:
            my_set.add(value)
        else:
            print("Ta wartość już występuje w zbiorze. \n")

    elif command == "usuń":
        value = input("Podaj wartość do usunięcia \n")
        if value not in my_set:
            print("Nie ma takiej wartości w zbiorze. \n")
        else:
            my_set.remove(value)

    elif command == "wyświetl":
        for index, value in enumerate(my_set):
            print(f"{index}. {value} \n")

    elif command == "wyjście":
        break

    else:
        print("Nie ma takiej komendy. \n")
