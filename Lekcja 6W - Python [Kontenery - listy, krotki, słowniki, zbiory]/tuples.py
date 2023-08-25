# Co zrobimy / Co chcemy uzyskać
# 1 - dodawać elementy do krotki
# 2 - wyświetlać elementy w krotce wraz z indeksami

my_tuple = ()

while True:
    command = input("Podaj komendę: \n")

    if command == "stwórz":
        n = int(input("Ile elementów ma znajdować się w liście: \n"))
        lista = []
        for i in range(n):
            value = input(f"Podaj wartość {i}: ")
            lista.append(value)
        my_tuple = tuple(lista)    # zamiana listy na krotkę

    elif command == "wyświetl":
        index = int(input("Podaj index: \n"))
        if len(my_tuple) - 1 >= index:
            print(my_tuple[index])
        else:
            print("Tego indeksu nie ma w tej krotce. \n")

    elif command == "exit":
        break

    else:
        print("Nie ma takiej komendy. \n")
    