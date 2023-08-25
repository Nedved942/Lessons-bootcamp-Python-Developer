# ZADANIE 1

"""
Stwórz program, który na podstawie

tabeli inflacji wartości
oprocentowania kredytu,
kwoty początkowej kredytu
stałej wartości raty
wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację) i kwota raty były pobierane ze standardowego wejścia (terminal).

Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.

Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium powinno zawierać więcej, niż jeden commit.
"""


initial_credit_value = float(input("Podaj wysokość kredytu: "))
credit_perc = float(input("Oprocentowanie kredytu: "))
rate_value = float(input("Kwota raty: "))

inflation_1 = 1.59282448436825
inflation_2 = -0.453509101198007

# STYCZEŃ
credit_value_1 = (1 + ((inflation_1 + credit_perc)/1200)) * initial_credit_value - rate_value
print(credit_value_1)
print(f"Twoja pozostała kwota kredytu to {credit_value_1}, to {initial_credit_value - credit_value_1} mniej niż w poprzednim miesiącu.")

# LUTY
credit_value_2 = (1 + ((inflation_2 + credit_perc)/1200)) * credit_value_1 - rate_value
print(credit_value_2)
print(f"Twoja pozostała kwota kredytu to {credit_value_2}, to {credit_value_1 - credit_value_2} mniej niż w poprzednim miesiącu.")


# Zaokrąglanie - tak na marginesie

credit_value_x = input("Wpisz wartość: ")
credit_value_x_real = round(credit_value_x, 2)
print(credit_value_x_real)


# Do czego warto zajrzeć?
# 1. f-strings
# 2. typy zmiennych

# RealPython - źródło
