# Źródła : książka, lekcje z kursu, lekcje moje (będzie prawie to samo, ale jednak mogę przepatrzeć)

""" Python """
print()  # Wyświetlanie elementu na ekranie/konsoli
my_value = 3  # Definicja zmiennej
dir(my_value)  # Wylistuje wszystkie możliwe funkcje i parametry danej zmiennej/typu

""" Stringi """
example_text = "Jakis//tekst//z//kilkoma//elementami"
examp_text_2 = example_text + " i drugi tekst, który połączyłem (skonkatenowałem)."  # Konkatenacja (dodawanie stringów)
f"To jest fstring. Może wyświelać zmienne takie jak {example_text} lub {my_value}."  # Tzw. fstring (format string)
splitted_text = example_text.split("//")  # Dzieli tekst względem podanego separatora i zapisuje jako elementy do listy
joined_text = "___".join(splitted_text)  # Łączy elementy listy z użyciem podanego separatora
print(example_text.find("tekst"))  # Wskazuje na indeks w jakim znalazło element
print(example_text.lower())  # Zamienia tekst na małe litery
print(example_text.upper())  # Zamienia tekst na duże litery
print(example_text.swapcase())  # Zamienia małe litery na duże i na odwrót
print("tekst z małych liter".capitalize())  # Pierwsza litera ma być duża
print(example_text.casefold())  # Zamienia tekst na małe litery (różni się od .lower m.in. zamianą znaków niełacińskich)
print(example_text.center(100, "-"))  # Centruje tekst na daną długość i wypełnia podanym elementem
print(example_text.rjust(100, "-"))  # Justuje tekst do prawej
print(example_text.ljust(100, "-"))  # Justuje tekst do lewej
print(example_text.count("e"))  # Zlicza ilość wystąpień danego znaku/elementu
print(example_text.endswith("ami"))  # Sprawdza czy tekst kończy się konkretnym elementem
print(example_text.startswith("Jak"))  # Sprawdza czy tekst zaczyna się się konkretnym elementem
print(example_text.removeprefix("Jakis"))  # Usuwa podany znak/element z początku tekstu
print(example_text.removesuffix("//elementami"))  # Usuwa podany znak/element z końca tekstu
print(example_text.replace("//", " "))  # Zamiana podanych elementów w tekście na inny podany element
print(example_text.islower())  # Sprawdza czy cały tekst jest z małych liter
print(example_text.isupper())  # Sprawdza czy cały tekst jest z dużych liter
print(example_text.isnumeric())  # Sprawdza czy tekst jest numerem (jest wartością numeryczną)

""" Listy """
my_list = []  # Definicja listy
my_list_two = list()  # Definicja listy - drugi sposób
my_list.append(my_value)  # Dodanie elementu do listy
my_list = my_list[::-1]  # Odwracanie listy
my_list.reverse()  # Odwrócenie listy na stałe


""" Słowniki """
my_dictonary = {}  # Definicja słownika
my_dictionary_two = dict()  # Definicja słownika - drugi sposób
my_dictonary["key"] = "value"  # Dodanie pary klucz-wartość do słownika


""" Metody magiczne """


""" Generatory """


""" Dekoratory """
# @staticmethod  # Metoda statyczna - pozwala odwoływać się do funkcji z poziomu klasy a nie z poziomu obiektu
# Dzięki tej metodzie można "stworzyć" metodę, która nie wymaga self, czyli argumentu odnoszącego się do danego obiektu


""" Instrukcja with open"""


""" Biblioteki wbudowane """
""" CSV """


""" JSON """
import json

json.dumps(my_dictonary)  # Serializacja/konwersja dowolnego typu danych na typ json
data_json = json.dumps(my_dictonary)
json.loads(data_json)  # Serializacja/konwersja typu json na docelowy typ danych


""" RANDOM """


""" DATETIME """
import datetime
# Date - operacje na datach (bez godzin, tylko daty)
# Datetime - operacje na dniach i godzinach
# Timedelta - np. różnice dat

datetime.date.today()  # Zwraca dzisiejszą datę (jako obiekt datetime.datetime)
some_date = datetime.date.today()
date_as_string = str(some_date)
datetime.date.fromisoformat(date_as_string)  # Serializacja na obiekt datetime.datetime
datetime.timedelta(days=1)  # Zwraca różnicę jednego dnia, którą później można dodać lub odjąć od innej daty
some_date.strftime("%d-%m-%Y")  # Zamiana obiektu datetime.datetime na string w podanym formacie
datetime.datetime.now()  # Zwraca obecną godzinę i dzień
datetime.datetime.now().time()  # Zwraca tylko obecną godzinę
datetime.datetime.now().date()  # Zwraca tylko obecny dzień

""" TIME """


""" COPY """


""" PPRINT """


""" SYS """


""" OS """


""" Biblioteki zaimplementowane """
""" REQUESTS """









