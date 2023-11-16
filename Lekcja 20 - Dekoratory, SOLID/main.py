""" Moje notatki """

def say_hello():
    print("Hello!")


print(say_hello)  # Odwołujemy się do obiektu funkcji (miejsca gdzie jest ulokowana w pamięci)


# cache - dekorator
# Po wykonaniu operacj, jej wynik jest zapamiętywany w pamięci


# functools - biblioteka, zbiór różnych pythonowych funkcjonalności nieskategoryzowanych


# Zadaniem dekoratora jest zmodyfikowanie danych wejściowych lub dodanie jakiegoś działania do funkcjonalności
# Używa się ich po to, aby nie było potrzeby modyfikacji napisanych już funkcji i aby można było przypisać jakieś
# działanie/funkcjonalność do wielu funkcji.


""" Kod lekcji z FC """

import os


def bordered(callback):
    w, h = os.get_terminal_size()
    print("=" * w, end="\n\n")
    callback()
    print()
    print("=" * w, end="\n\n")


def main_func():
    print("Line 1")
    print("Line 2")


bordered(main_func)
print(os.get_terminal_size())

def other_func():
    print("Line 3")
    print("Line 4")