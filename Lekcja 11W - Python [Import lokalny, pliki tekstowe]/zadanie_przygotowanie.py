"""
NAJPIERW ZADANIE Z LEKCJI 5
"""

balance = 12000  # Stan konta
history = []  # Historia operacji
warehouse = {}


# CZĘŚĆ LOGIKI ZADANIA
balance -= 200
balance += 250  # Operacje na saldzie konta

history.append("Wykonano operację zakupu.")
history.append("Zwiększono saldo konta o xxxxx")  # Zapisanie do historii wykonanych operacji

warehouse["rower"] = {
    "price": 800,
    "quantity": 2
}
warehouse["hulajnoga"] = {
    "price": 250,
    "quantity": 6
}
# KONIEC LOGIKI ZADANIA

# Zapisanie do pliku istniejących danych w odpowiednim miejscu
# Odczytanie z pliku istniejących danych w odpowiednim miejscu