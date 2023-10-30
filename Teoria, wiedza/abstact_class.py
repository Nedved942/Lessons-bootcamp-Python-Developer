"""
Biblioteka abc w języku Python odnosi się do modułu o nazwie "Abstract Base Classes", co można przetłumaczyć jako
"Klasy Bazowe Abstrakcyjne". Ta biblioteka jest częścią standardowej biblioteki Pythona i umożliwia tworzenie klas
abstrakcyjnych oraz definiowanie abstrakcyjnych metod w taki sposób, który umożliwia sprawdzanie, czy konkretne klasy
dziedziczące implementują te metody.

Klasy abstrakcyjne to klasy, które same w sobie nie posiadają pełnej implementacji, ale zawierają pewne deklaracje
metod, które muszą być zaimplementowane w klasach dziedziczących. W Pythonie klasa abstrakcyjna jest tworzona za pomocą
modułu abc i jego klas bazowych.

Najważniejszą klasą w module abc jest ABC (Abstract Base Class). Dzięki niej możesz tworzyć własne klasy abstrakcyjne.
Klasa abstrakcyjna może zawierać abstrakcyjne metody, które nie mają domyślnej implementacji. Klasa dziedzicząca po
takiej klasie abstrakcyjnej musi dostarczyć implementację tych abstrakcyjnych metod, inaczej otrzymasz błąd w momencie
próby jej utworzenia.
"""

"""
Oto przykład wykorzystania modułu abc do stworzenia klasy abstrakcyjnej i dziedziczenia po niej:
"""

from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def obwod(self):
        pass


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * 3.14 * self.promien


kolo = Kolo(5)
print(kolo.obwod())  # Wywołanie metody obwod() dla obiektu klasy Kolo

"""
W powyższym przykładzie klasa Figura jest klasą abstrakcyjną zawierającą abstrakcyjną metodę obwod(). Klasa Kolo
dziedziczy po klasie Figura i implementuje tę abstrakcyjną metodę. Dzięki temu możemy tworzyć obiekty klasy Kolo i
wywoływać jej metody.

Jeśli nie dostarczymy implementacji dla abstrakcyjnej metody, Python wygeneruje błąd, co pomaga w zapewnieniu, że
wszystkie wymagane metody są zaimplementowane w klasach dziedziczących.
"""
