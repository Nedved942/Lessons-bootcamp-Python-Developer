"""
Główne różnice w wydajności między listami a tuplami:

Operatory "in", "not in" są znacząco szybsze w tuplach
Tworzenie tupli jest znacząco szybsze niż tworzenie listy
Porównywanie dwóch tupli jest znacząco szybsze niż porównywanie dwóch list.
"""

"""
Tuple mogą być przekształcane w listy, a listy w tuple.
"""
mixed_tuple = "a", 1, "b", 2, True
mixed_list = list(mixed_tuple)

mixed_list2 = ["a", 1, "b", 2, True]
mixed_tuple2 = tuple(mixed_list2)

"""
Raz zadeklarowane nie mogą być modyfikowane
"""

"""
Tuple z pojedynczym elementem
"""
my_tuple = (5,)


"""
Funkcja enumerate() jako argument pobiera listę i zwraca generator, który po zamianie na listę, zwraca listę krotek, 
gdzie pierwszy element krotki jest indeksem, a drugi wartością oryginalnej listy
"""

"Następująca deklaracja jest jak najbardziej prawidłowa:"

a, b = 1, 2
print(a)
print(b)

"""
Jest to możliwe dzięki wewnętrznemu użyciu tupli. Innymi słowy indeksy tupli mogą być zdefiniowane po obu stronach operatora przypisania
Podobnie z wcześniejszą deklaracją tupli
"""

t1 = 1, 2
a, b = t1
print(t1)
print(a)
print(b)
