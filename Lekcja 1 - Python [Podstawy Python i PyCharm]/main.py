print("Hello World")


ZmiennaString = "Adam Nowak"

first_name = "Adam"

age = 45    # int
number = 3.67   # float

is_adult = False    # bool

test = None     # NoneType

print(ZmiennaString, first_name, age, number, is_adult, test)

bigNote = """
Dużo tekstu
Jeszcze więcej tekstu w innej linijce
"""

print(bigNote)

userNumber1 = input("Podaj liczbę 1: ")
userNumber2 = input("Podaj liczbę 2: ")
print(userNumber1, userNumber2)

userNumber1 = int(userNumber1)
userNumber2 = int(userNumber2)
print(f"Wpisałeś wartość {userNumber1}, a także {userNumber2}. Teraz podam ich sumę.")

suma = userNumber1 + userNumber2
print(f"suma = {suma}")
