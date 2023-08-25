# Funkcje, obiekty, PEP


# PEP - dane zasady pisania czystego kody w języku Python.
# Te zasady można wyszukać. Możesz to sobie przejrzeć i wydrukować.
# Interpreter zaznacza błędy PEP i wypisuje treść. Nie powodują one wysypania programu, natomiast jest to błąd czystości kodu.

"""Poprawnie napisany kod zgodnie z PEP8"""
some_pep8_value = 12  # Nazwa zmiennej jest z podkreślników




# Funkcje
# def - define - zdefiniuj (funkcję)

# """
# def print
#
# """
#
#
# def print_separator():
#     print("*" * 50)
#     print("-" * 50)
#     print("*" * 50)
#
#
# """Wykonanie funkcji"""
# print("Jakiś tekst")
# print_separator()
# print("Jakiś tekst")
# print_separator()
# print("Jakiś tekst")
#
#
# """Funkcja z argumentami"""
# def print_name(my_name):
#     print(f"Hello {my_name}!")
#
# print_name("Paweł")

def calculate_bmi(weight, height):
    calculate_bmi = (weight / (height / 100) ** 2)
    print(calculate_bmi)