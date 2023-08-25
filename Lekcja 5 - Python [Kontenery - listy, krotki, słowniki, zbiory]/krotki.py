# Pratyczna uwaga - Tuple są szybsze, szybciej obsługiwane przez Pythona

empty_tuple = ()
empty_tuple2 = tuple()

integer_tuple = 1, 2, 3, 4

x = 3.5
mixed_tuple = ("a", x, 2, True)

single_tuple = ("Napis")


# Konwersja / zamiana krotki na listę i odwrotnie
mixed_list = list(mixed_tuple)
mixed_tuple = tuple(mixed_list)


list_of_tuples = [
    ("Bazyli", "Chodor"),
    ("Janusz", "Kowalski")
]

for first_name, last_name in list_of_tuples:
    print(f"{first_name} {last_name}")