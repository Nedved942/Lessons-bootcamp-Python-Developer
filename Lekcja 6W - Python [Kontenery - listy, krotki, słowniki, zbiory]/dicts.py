# Co zrobimy / Co chcemy uzyskać
# 1 - dodawać elementy do słownika
# 2 - usuwać elementy ze słownika
# 3 - edytować elementy w słowniku

my_dictionary = {}

while True:
    command = input("Wprowadź komendę: \n")

    if command == "dodaj":
        key = input("Podaj klucz: \n")
        if key not in my_dictionary.keys():
            value = input("Podaj wartość: \n")
            my_dictionary[key] = value
            print(f"Dodano wartość do słownika {key} : {my_dictionary[key]} \n")
        else:
            print("Klucz już istnieje w tym słowniku. \n")

    elif command == "usuń":
        key = input("Podaj klucz: \n")
        if key not in my_dictionary.keys():
            print("Nie ma takiego klucza. \n")
        else:
            # dictionary.remove(key)
            del my_dictionary[key]
            # name = dictionary.pop(key)            # Usuwa klucz i wartość metodą .pop i zapisuje go do zmiennej
            # print(f"Usunięto {key} : {name} \n")

    elif command == "edytuj":
        key = input("Podaj klucz: \n")
        if key not in my_dictionary.keys():
            print("Nie ma takiego klucza. \n")
        else:
            value = input("Podaj nową wartość \n")
            my_dictionary[key] = value
            print(f"Nowa wartość klucza {key} to {my_dictionary[key]} \n")

    elif command == "exit":
        break

    else:
        print("Nie ma takiej komendy.", sep="\n")   # Inny sposób na new line
