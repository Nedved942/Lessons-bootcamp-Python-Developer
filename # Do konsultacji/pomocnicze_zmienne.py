# Pomocnicza zmienna str_package modyfikująca tekst w podsumowaniu
if packages > 4:
    str_package = "paczek"
elif packages > 1 and packages <= 4:
    str_package = "paczki"
else:
    str_package = "paczkę"

"""
Gdzie się używa sformułowań powyższego typu?
Czy jest to zapisane poprawnie, czy tak się stosuje?
Czy lepiej było by to zamieścić np. w klasie lub w innym pliku żeby nie zaśmiecać kodu?
"""