# zmienna_string = "azegarek,"
# zmienna_string = zmienna_string.removesuffix(",")
# zmienna_string = zmienna_string.removeprefix("a")
#
# print(zmienna_string)


"""
Wyjątki
"""

#  Dzielenie przez zero

# def divide_values(first_value, second_value):
#     return first_value / second_value
#
# try:
#     print(divide_values(1, 2))
#     print(divide_values(2, 1))
#     print(divide_values(2, 0))
#     print(divide_values(1, 0))
# except:
#     print("Błąd")


def divide_values(first_value, second_value):
    try:
        return first_value / second_value
    except ZeroDivisionError:
        return "Błąd - dzielenie przez 0"
    except TypeError:
        return "Błąd - niepoprawne typy w operacji"
    except:
        return "aa"



