"""
Przykładowe wbudowane pakiety:
- math
- random
- copy (jedna z najważniejszych)
- pprint
- sys
- os
- csv

"""

#
# import random
#
# randomized_integer = random.randint(4, 8)
#
# random_element_from_range = random.randrange(0, 100, 4)  # Losuje element od 0 do 100, ale "skacze" co 4 elementy
# print(random_element_from_range)
#
#
#
# """
# Copy
# """
#
# import copy
# some_dict = {"aa": 12}
# copied_dict
#

"""
pprint - "pretty print"
"""

# from pprint import


"""
sys
"""

import sys

print(sys.platform)  # System operacyjny
print(sys.path)  # Ścieżka
print(sys.argv)  # Argumenty wejściowe dla skryptu Pythona
print(sys.api_version)
size_of_very_large_complex_dict = sys.getsizeof(very_large_complex_dict)


print(sys.argv) # sys.argv to lista, której elementami są podane argumenty przez użytkownika w konsoli po danej komendzie, w tym przypadku 'python', służącej do odpalenia programu

file_name, first_name, last_name, age = sys.argv    # listę sys.argv z argumentami można przypisać do zmiennych w kodzie w taki sposób
_, first_name, last_name, age = sys.argv             # pierwszy element w liście, czyli pierwszy argument jest to zawsze nazwa programu (pliku.py, który uruchamiamy). Jest on zwykle nieużywany, więc do jego przypisania wykorzystuje się często znak '_'
first_name, last_name, age = sys.argv[1:]            # można też zrobić to w lepszy sposób, poprzez ucięcie listy z pierwszego elementu. Wtedy już nie przypisujemy go do zmiennej.
