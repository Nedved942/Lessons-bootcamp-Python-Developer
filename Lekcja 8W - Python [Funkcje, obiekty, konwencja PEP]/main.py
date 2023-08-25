
# TODO Jakiś specjalny komentarz.

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self): # Metoda magiczna pozwalająca na wyświetlanie wybranych danych w trakcie wyprintowania obiektu (zamiast nazwy obiektu i miejsca w pamięci)



x = Student("Mati", "Borek")    # Tworzenie obiektu i przypisanie do zmiennej
Student("Paweł", "Benek")      # Obiekt utworzy się w pamięci komputera