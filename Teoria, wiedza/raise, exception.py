"""
Wytłumaczysz mi jak w Pythonie stosuje się wyjątki za pomocą definicji klasy dzedziczonej z Exception i wywołania wyjątku za pomocą słowa kluczowego raise?
"""

"""
ChatGPT
Oczywiście! W Pythonie wyjątki są mechanizmem służącym do obsługi błędów i nieoczekiwanych sytuacji w kodzie. Możesz tworzyć własne wyjątki, dziedzicząc je z klasy Exception lub jej podklas.

Oto kroki, jakie musisz podjąć, aby użyć wyjątków za pomocą definicji klasy dziedziczącej z Exception i wywołania wyjątku za pomocą słowa kluczowego raise:

Definiowanie własnego wyjątku:
Możesz zacząć od zdefiniowania własnej klasy wyjątku, która dziedziczy z klasy Exception. Możesz nadać swojej klasie dowolną nazwę, ale zazwyczaj dodaje się sufiks "Error" do nazwy klasy, aby jasno wskazać, że jest to klasa wyjątku. Na przykład:
"""
class MojaWlasnaKlasaWyjatku(Exception):
    def __init__(self, wiadomosc):
        self.wiadomosc = wiadomosc
"""
W powyższym przykładzie MojaWlasnaKlasaWyjatku jest własnym wyjątkiem, który dziedziczy po klasie Exception i posiada niestandardowy konstruktor, który przyjmuje wiadomość jako argument.

Wywoływanie wyjątku za pomocą raise:
Aby wywołać własny wyjątek, używasz słowa kluczowego raise, a następnie tworzysz instancję swojej klasy wyjątku i przekazujesz mu odpowiednią wiadomość. Na przykład:

"""
def funkcja_generujaca_blad():
    raise MojaWlasnaKlasaWyjatku("To jest moj wlasny wyjatek!")
"""
W powyższym przykładzie funkcja_generujaca_blad generuje własny wyjątek, wywołując MojaWlasnaKlasaWyjatku z odpowiednią wiadomością.

Obsługa wyjątku:
Aby obsłużyć wyjątek, możesz użyć bloku try i except. W ten sposób unikniesz awarii programu i będziesz mógł podjąć odpowiednie działania w przypadku wystąpienia wyjątku. Na przykład:

"""

try:
    funkcja_generujaca_blad()
except MojaWlasnaKlasaWyjatku as e:
    print(f"Zlapalem wyjatek: {e.wiadomosc}")

"""    
W tym przypadku, jeśli funkcja funkcja_generujaca_blad wywoła własny wyjątek, to zostanie on złapany przez blok except, a następnie zostanie wyświetlona wiadomość zawarta w wyjątku.

To jest ogólny sposób na tworzenie i obsługę własnych wyjątków w Pythonie. Możesz dostosować swoje klasy wyjątków i ich obsługę do konkretnych potrzeb w swoim kodzie.
"""

"""
User
zazwyczaj dodaje się sufiks "Error" do nazwy klasy - możesz to rozszerzyć i podać przykład?
"""

"""
ChatGPT
Oczywiście, oto przykład, który rozszerza ideę dodawania sufiksu "Error" do nazwy klasy wyjątku:
"""

class MojaBladnaOperacja(Exception):
    def __init__(self, wiadomosc):
        self.wiadomosc = wiadomosc

def dzielenie(a, b):
    if b == 0:
        raise MojaBladnaOperacja("Nie można dzielić przez zero!")
    return a / b

try:
    wynik = dzielenie(10, 0)
except MojaBladnaOperacja as e:
    print(f"Wystąpił błąd: {e.wiadomosc}")

"""
W tym przykładzie utworzono własną klasę wyjątku o nazwie MojaBladnaOperacja. Chociaż nazwa klasy nie zawiera dokładnie sufiksu "Error", to jest ona nadal zrozumiała i wyraźnie wskazuje na błąd lub wyjątkową sytuację związaną z operacją dzielenia. Gdy funkcja dzielenie zostanie wywołana z b = 0, zostanie zgłoszony wyjątek MojaBladnaOperacja, który następnie jest obsługiwany w bloku except, a jego wiadomość jest wyświetlana na konsoli.
"""

"""
User
Ok, czyli własne wyjątki najlepiej nazywać słowem lub wyrażeniem, którym jest skutek wywołania danego błędu, czyli np. InvalidInput, mam rację?
"""

"""
ChatGPT
Tak, jesteś całkowicie prawidłowy. Dobrą praktyką jest nadawanie swoim własnym klasom wyjątków opisowych nazw, które jasno wskazują na przyczynę błędu lub rodzaj sytuacji wyjątkowej, z którą mamy do czynienia. To sprawia, że kod staje się bardziej czytelny i ułatwia debugowanie oraz obsługę błędów.

Oto kilka przykładów dobrych nazw klas wyjątków:

InvalidInputError: Możesz użyć tej nazwy, gdy użytkownik podaje niepoprawne dane wejściowe.

FileNotFoundError: Ta nazwa jest stosowana, gdy nie można znaleźć określonego pliku.

ConnectionError: Możesz użyć tej nazwy, gdy wystąpi problem z połączeniem do zasobu zdalnego, na przykład baz danych lub serwera.

PermissionDeniedError: Ta nazwa wskazuje na sytuację, w której użytkownik nie ma odpowiednich uprawnień do wykonania danej operacji.

Korzystanie z opisowych nazw klas wyjątków pomaga innym programistom (w tym tobie samemu w przyszłości) zrozumieć naturę błędu i ułatwia obsługę wyjątków w kodzie. To dobra praktyka, która przyczynia się do zwiększenia czytelności i jakości kodu.
"""
