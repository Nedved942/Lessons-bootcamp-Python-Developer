# Źródła : książka, lekcje z kursu, lekcje moje (będzie prawie to samo, ale jednak mogę przepatrzeć)

""" Python - moduł bultins (funkcje wbudowane) """
print()  # Wyświetlanie elementu na ekranie/konsoli
my_value = 3  # Definicja zmiennej
len("Napis")  # Funkcja wyliczająca długość zmiennej/elementu
input("Wprowadź dane: ")  # Pobiera dane z klawiatury od użytkownika
int(my_value)  # Konwersja typu danych (serializacja) na typ int
float(my_value)  # Konwersja typu danych (serializacja) na typ float
bool(my_value)  # Konwersja typu danych (serializacja) na typ bool
str(my_value)  # Konwersja typu danych (serializacja) na typ string
dir(my_value)  # Wylistuje wszystkie możliwe funkcje i parametry danej zmiennej/typu
# in
# not in
id(my_value)  # Wskazuje na miejsce w pamięci zarezerwowane na dany obiekt
# pass
# break
# continue


""" Stringi """
example_text = "Jakis//tekst//z//kilkoma//elementami"
examp_text_2 = example_text + " i drugi tekst, który połączyłem (skonkatenowałem)."  # Konkatenacja (dodawanie stringów)
f"To jest fstring. Może wyświelać zmienne takie jak {example_text} lub {my_value}."  # Tzw. fstring (format string)
f"Zmienna odczytana jako float i podana do 25 miejsc po przecinku: {my_value:.25f}"  # Formatowanie zmiennej w fstring
# Opisz .format i sposoby użycia
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
print("   a    ".strip())  # Usuwa znaki odstępu (spacji) umieszczone na początku i na końcu łańcucha znaków
print("   a    ".lstrip())  # Usuwa znaki odstępu (spacji) umieszczone na początku łańcucha znaków
print("   a    ".rstrip())  # Usuwa znaki odstępu (spacji) umieszczone na końcu łańcucha znaków
print(example_text.index("s"))  # Zwraca indeks pierwszego wystąpienia znaku w łańcuchu. Jeśli nie ma zgłosi wyjątek.


""" Listy """
my_list = []  # Definicja listy
my_list_two = list()  # Definicja listy - drugi sposób
my_list.append(my_value)  # Dodanie elementu do listy
my_list = my_list[::-1]  # Odwracanie listy
my_list.reverse()  # Odwrócenie listy na stałe
list(my_list)  # Konwersja typu danych na listę (np. z tuple)
all(my_list)  # Zwraca True, jeśli wszystkie wartości w liście są True
# .remove()
# .pop()


""" Krotki """
my_tuple = ()  # Definicja krotki
my_tuple_only_one_element = (5,)  # Krotka z jednym elementem


""" Słowniki """
my_dictonary = {}  # Definicja słownika
my_dictionary_two = dict()  # Definicja słownika - drugi sposób
my_dictonary["key"] = "value"  # Dodanie pary klucz-wartość do słownika
my_dictonary.get("key")  # Sprawdza czy dany klucz jest w słowniku [zwraca "value"]
my_dictonary.get("d")  # Sprawdza czy dany klucz jest w słowniku [zwraca None]
my_dictonary.get("d", False)  # Sprawdza czy dany klucz jest w słowniku [zwraca False]
dict(my_dictonary)  # Konwersja typu danych na słownik
is_key_in_dict = "key" in my_dictonary  # sprawdza czy dany klucz jest w słowniku [zwraca True]
is_value_in_dict = "value" in my_dictonary.values()  # sprawdza czy dana wartość jest w słowniku [zwraca True]
del my_dictonary["key"]  # Usuwa klucz-wartość ze słownika


""" Zbiory """
my_set = set()  # Definicja pustego zbioru
sample_set = {"a", "b", "c", 1, True, ("a1", "a2", "a3")}  # Definicja zbioru z wartościami - jedyny sposób


""" Metody magiczne """


""" Generatory """


""" Dekoratory """

from functools import wraps, lru_cache

# @staticmethod  # Metoda statyczna - pozwala odwoływać się do funkcji z poziomu klasy a nie z poziomu obiektu
# Dzięki tej metodzie można "stworzyć" metodę, która nie wymaga self, czyli argumentu odnoszącego się do danego obiektu

# @property  # Dekorator również używany w definicji klas. Po jego użyciu przy definicji funkcji, można wywołać ją jako
# zmienną (atrybut - tylko do odczytu). Taką funkcję wywołujemy bez nawiasów i bez podawania argumentów (tak jak zwykłą
# zmienną.

# @cache

# @lru_cache

# @wrapps  # Dekorator służący do użycia przy tworzeniu dekoratorów w celu ich zabezpieczenia i stabilności.
# Bez użycia @wraps, funkcje dekorowane mogą utracić pewne informacje, takie jak nazwa funkcji, docstring itp.


# Baza do stworzenia dekoratora
def operation_time(callback):
    @wraps(callback)
    def wrapper():  # Tutaj jak i
        callback()

    return wrapper


""" Instrukcja with open"""


"""Raise"""


class MyError(Exception):  # Przykładowa definicja wyjątku
    def __str__(self):
        return "Unexpected file format"


""" Biblioteki wbudowane: """

""" CSV """
import csv

# csv.writer()
# csv.reader()
# metoda writerow()

""" JSON """
import json

json.dumps(my_dictonary)  # Serializacja/konwersja dowolnego typu danych na typ json
data_json = json.dumps(my_dictonary)
json.loads(data_json)  # Serializacja/konwersja typu json na docelowy typ danych

# json.dump()
# json.load()


""" RANDOM """
import random

random.randint(0, 100)  # Losuje wartość typu int z podanego przedziału liczbowego
random.choice(my_list)  # Losuje dany element z kontenera (np. z listy)
random.random()  # Losuje dowolną liczbę float z przedziału 0-1
random.seed()  # Unikalne dane, które oduzależniają random od naszego procesora
random.shuffle(my_list)  # Miesza kolejność w sekwencji/kontenerze


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
import time

time.time()  # Zwraca tzw. Epoch Time, czyli liczbę sekund mierzoną od 1 stycznia 1970 roku, 00:00:00 UTC do czasu
# wykonania operacji
time.perf_counter()  # Perfekcyjny licznik # Zwraca liczbę zmiennoprzecinkową reprezentującą czas w sekundach z
# dokładnością do frakcji mikrosekundy. Przydatny w bardziej dokładnych obliczeniach, np. czasu wykonania operacji


""" COPY """
import copy

copied_value = copy.copy(my_value)  # Płytka kopia tzw. Shallow Copy
copied_value = copy.deepcopy(copied_value)  # Głęboka kopia (bardziej zaawansowana, ale bardziej pamięciożerna)
# Używane do kopiowania obiektów mutowalnych


""" PPRINT """
import pprint

pprint.pprint(my_dictonary)  # "Pretty print" estetyczne formatowanie wyjść, często stosowane np. dla słowników dla
# lepszej czytelności
pprint.pp(my_dictonary)  # Dokładnie to samo polecenie co wyżej. Krótszy alias wprowadzony dla wygody na stałe do
# biblioteki jako funkcja pprint()


""" SYS """
import sys

list_of_inputs = sys.argv  # Zwraca listę argumentów wejściowych podanych w konsoli ("0" element to nazwa
# uruchamianego pliku)
sys.getsizeof(my_list)  # Zwraca rozmiar danego obiektu w bajtach
path_variable = sys.path  # Zwraca listę ścieżek, które Python przeszukuje w poszukiwaniu modułów do importowania.
# Można ją dynamicznie modyfikować w czasie wykonywania programu.
name_of_system = sys.platform  # Zwraca nazwę systemu operacyjnego, na której działa Python, np. linux, win32,
# darwin (MacOS).


""" OS """
import os

os.path.join("Users", "D2", "123.txt")  # Tworzy ścieżkę pliku kompatybilną z używanym systemem


""" MATH """
import math

math.floor(my_value)  # Zaokrągla liczbę w dół.
math.ceil(my_value)  # Zaokrągla liczbę w górę.
math.fabs(my_value)  # Zwraca wartość absolutną (z pominięciem +/- na początku).
math.log(my_value, base=2.71)  # Zwraca logarytm danej liczby. Jeśli parametr base nie jest podany, zwraca logarytm
# naturalny
math.sin(my_value)  # Zwraca sinus liczby (w radianach).
math.cos(my_value)  # Zwraca cosinus liczby (w radianach).
math.fsum([1, 2, 3])  # Zwraca sumę wszystkich elementów.
math.pow(my_value, 2)  # Metoda potęgująca.


""" STATISTICS """
import statistics

statistics.median(my_list)  # Zwraca medianę podanych wartości
statistics.mean([1, 2, 3])  # Zwraca średnią podanych wartości
statistics.mode(my_list)  # Zwraca dominantę podanych wartości


""" KEYWORD """
import keyword

keyword.iskeyword(example_text)  # Sprawdza czy dany ciąg znaków jest słowem kluczowym w Pythonie


""" Biblioteki zaimplementowane: """

""" REQUESTS """

""" FLASK """

""" PANDAS """

""" PYGAME """
