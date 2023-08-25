lista = []      # Pierwszy sposób definicji pustej listy - bardziej popularny
lista2 = list() # Drugi sposób definicji pustej listy

x = 3
lista_liczby = [1, 65, 3.6, x, -2, 0]

first_name = "Marek"
lista_tekst = ["Hello World", "Ania", "x", first_name]

lista_rozne_wartosci = [x, first_name, False, None, 35.4, "znak", lista_tekst, lista_liczby] # W liście mogą być wszystkie wartości, a także inne listy i inne kontenery

print(lista_liczby, lista_tekst)
print(lista_rozne_wartosci)


print(lista_liczby[0])              # Pierwszy index jest wartością 0
print(lista_liczby[2])
print(lista_liczby[-1])             # Odczytanie ostatniej wartości z listy. Podawanie wartości indeksu z minusem powoduje odczyt wartości od końca listy
print(lista_rozne_wartosci[6][2])   # Dwuwymiarowa lista. Można się odwołać do indeksu w drugim kontenerze (jeśli jest dwuwymiarowa)

# WAŻNY TIP - Stosowany w praktyce
# Listę można zapisać w sposób bardziej czytelny kiedy wymaga tego sytuacja, np. jest wiele wymiarów lub wiele zmiennych o długich nazwach

lista_czytelny_zapis = [
    x,
    True,
    2,
    65,
    lista_tekst
    [
        3,
        56,
    ]
]

long_list = [x, 3]
lenght_long_list    # Dokończ - dwa sposoby uzyskania ostatniej wartości z listy . len()


for wartosc_lista_liczy in lista_liczby:
    print(wartosc_lista_liczy)

for index in [0, 1, 2, 3]:
    print(index)


polaczona_lista = lista_liczby + lista_tekst
print(polaczona_lista)

lista_rozne_wartosci.append("Dodany string")    # Dokończ
# lista_rozne_wartosci.