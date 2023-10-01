""""""  # tzw. doc string, ma on także inne zastosowanie niż komentarz kodu. Można wywołać go jako dokumentację
        # metodą magiczną __doc__ tak jak w poniższym kodzie


class TestClass:
    """
    Test
    """
    ...


test_class = TestClass()
print(test_class.__doc__)



#  Metoda prywatna
#  Kompozycja - wywołanie danego obiektu jako parametr w inneym obiekcie/klasie

...  # Elipsis  -->  Stosuje się zamiennie z pass? Tylko elipsis zwraca type elipsis


# PyTest - biblioteka do testowania
# Do testów jednostkowych (dla programistów)