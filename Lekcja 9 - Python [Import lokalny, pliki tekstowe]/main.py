"""
Import lokalny
"""

# SPOSÓB 1: Import całego pliku
import functions

print("Jakiś test")
functions.print_separator()  # Wywołanie funkcji print_separator z pliku functions.py
print("Jakiś inny tekst")
functions.print_separator()
print("Jakiś jeszcze inny tekst")
functions.print_separator()

functions.print_hello_name("Paweł")  # Wywołanie funkcji print_hello name z pliku functions.py

print(functions.some_int)  # Odwołanie do zwykłej zmiennej

# SPOSÓB 2: Import częściowy
from functions import print_hello_name

print

