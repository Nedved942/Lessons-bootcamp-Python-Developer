# number = input("Liczba 1: ")
# number = int(number)

# print(type(number))

# print(type(4))        # class <int>
# print(type(True))     # class <bool>
# print(type(44.56))    # class <float>
# print(type(None))     # class <NoneType>
# print(type(0.00))     # class <float> !!

# print(bool(0))        # False
# print(bool(1))        # True - i dla każdego innego inta
#
# print(bool(3.65))     # True
#
# print(bool(""))       # False ! - tzw. "pusty string"
# print(bool("x"))      # True
#
# print(bool(None))     # False


# Sposoby formatowania stringów
# np. zamiana znaków w stringach jako zmiennych

"""
age = 34

name = "Adam {age}" # Aby zrobić fstringa potrzeba dodać f przed ""
print(name)

# Metoda fstring
name = f"Adam {age}" # fstring
print(name)

# Metoda 2
name2 = "Adam %i" % age
print(name2)

test = "TEST"
name3 = "Adam %i (%s)" % (age, test) # Więcej zmiennych musi być w nawiasach
print(name3)

# Metoda .format
print("Adam {}".format(age))
print("Adam {} ({})".format(age, test))
print("Adam {age} ({test})".format(age=age, test=test)) # Można przypisać odpowiedniki zmiennych w tekście
print("Adam {test} ({age})".format(age=age, test=test)) # Można także zamienić kolejność
"""

liczba = 256.235346
print("Wyświetl liczbę {liczba:.2f}")
