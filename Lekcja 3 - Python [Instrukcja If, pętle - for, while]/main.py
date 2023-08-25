"""
number = input("Podaj liczbę: ")
number = int(number)

# print(number)
# number = number * 2
# print(number)


if number >= 2:
    print("Number większe/równe od 2.")
"""

# Operatory porównania:
# >
# >=
# <
# <=
# ==
# !=

""""
if number != 3:
    print("Number różny od 3.")


name = input("Podaj imię: ")

if name == "Adam" or name == "Anna":
    print("To jest Adam lub Anna.")
elif name == "Jan":
    print("To jest Jan.")
else:
    print("To jest ktoś inny.")
"""

# Operatory logiczne:
# or
# and
# not

# is

"""
if True:
    print("Ta instrukcja warunkowa zawsze się wykona.")

name = input("Podaj imię: ")
if name:
    print("To się wykona dla każdego stringa oprócz pustego stringa, ponieważ pusty string daje False.")

liczba = input("Podaj liczbę: ")
if liczba:
    print("To się wykona dla każdego liczby oprócz 0, ponieważ 0 daje False.")

test = None
if test:
    print("To się nie wykona, ponieważ None zawsze daje False.")
"""

"""
number = input("Podaj liczbę:" )
number = int(number)

while number < 10:
    print("Number < 10")
    number += 1
    print(number)
"""

"""
list_of_person = []
number_of_person = 0
while True:
    print("#### MENU ####")
    print("1 - Dodaj osobę")
    print("2 - Pokaż osoby")
    print("3 - Wyjdź z programu")
    command = input("Podaj komendę: ")

    if command == "3":
        print("Wychodzę z programu")
        break
    elif command == "2":
        for person in list_of_person:
            number_of_person += 1
            print(f"{number_of_person}. {person}")
    elif command == "1":
        person = input("Wpisz imię osoby: ")
        list_of_person.append(person)
    else:
        print("Nieprawidłowa komenda. Wpisz wartość jedną z poniższych.")

    # komenda break przerywa pętle i kończy ją
    # komenda continue - podobna do break, aczkolwiek przerywa pętle i przechodzi do kolejnej iteracji (nie kończy jej, tylko kontynuuje :) )
    # komenda pass - nic nie robi, wypełniacz - pozwala zastosować jakąś pustą komedę warunkową lub pętlę, tzw. draft (szkic)
    """

print("test")

for letter in "Adam":
    print("TEST:", letter)

for number in range(10):
    print("TEST:", number)

for number in range(1, 11):
    print("TEST:", number)

for number in range(1, 11, 2):  # trzeci argument - krok , czyli co ile iteracji
    print("TEST:", number)

for number in range(10):
    if number == 7:
        break

for number in range(10):
    if number == 7:
        continue
    print(f"{number} - Wszystkie oprócz 7")
