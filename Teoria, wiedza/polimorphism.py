"""
Polimorfizm to jeden z kluczowych konceptów w programowaniu obiektowym, który pozwala na to, aby różne klasy mogły być
traktowane w spójny sposób, niezależnie od swojej konkretnej implementacji. Główne założenie polimorfizmu można opisać
zwięźle jako:

"Polimorfizm pozwala na wywoływanie tych samych metod na obiektach różnych klas, co umożliwia dostosowanie działania
metody do konkretnego typu obiektu, przy zachowaniu spójności interfejsu."


Oto kilka kluczowych punktów dotyczących polimorfizmu:

Spójny interfejs: Klasy, które implementują ten sam interfejs lub dziedziczą po wspólnej klasie bazowej, muszą zapewniać
te same metody. Dzięki temu można traktować je w spójny sposób, niezależnie od ich konkretnych implementacji.

Dynamiczne wywołanie metod: Polimorfizm umożliwia wywoływanie tych samych metod na obiektach różnych klas, bez potrzeby
sprawdzania ich konkretnego typu w trakcie wykonywania programu. To oznacza, że działanie metody zależy od rzeczywistego
typu obiektu, na którym jest wywoływana.

Uproszczona obsługa wielu typów: Dzięki polimorfizmowi można tworzyć bardziej ogólne i elastyczne funkcje oraz
algorytmy, które obsługują różne typy obiektów, bez potrzeby tworzenia oddzielnych wersji tych funkcji dla każdego typu.

Wielopostaciowość (ang. polymorphism): Istnieją dwa główne rodzaje polimorfizmu: polimorfizm oparty na dziedziczeniu
(np. przesłanianie metod) i polimorfizm oparty na interfejsach (np. interfejsy w języku Java lub klasy abstrakcyjne
w Pythonie). Oba te rodzaje pozwalają na różne formy wykorzystania polimorfizmu w zależności od potrzeb projektu.

Polimorfizm jest jednym z głównych założeń programowania obiektowego i pomaga tworzyć bardziej elastyczny i rozszerzalny
kod, który może łatwiej obsługiwać zmienne i rozbudowane struktury danych oraz zachowania.
"""
