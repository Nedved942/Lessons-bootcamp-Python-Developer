"""
Jak zrobić poprawnie sprawdzenie poniższego kodu metodą try-except? czy to jest dobrze sformułowane i czy można lepiej?
"""

is_element_to_send_int = False

while not is_element_to_send_int:
    elements_to_send = input("Podaj liczbę elementów do wysłania: ")
    is_element_to_send_int = True
    try:
        elements_to_send = int(elements_to_send)
    except:
        print("Podana wartość musi być liczbą.")
        is_element_to_send_int = False