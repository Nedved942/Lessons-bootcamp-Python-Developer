from flask import Flask  # Import głównej klasy Flask

app = Flask(__name__)


@app.route("/info")  # Odnośnik URL  (ogólnie jest to dekorator)
def info():
    return "Hello World! :)"


"""
Flask automatycznie ma zdefiniowane pewne nazwy np. 'app' dla aplikacji lub 'templates' dla szablonów
"""

"""
Tagi - przeglądarka czasem dodaje sama
Head - ustawienia strony

Body - wygląd strony
<h1> nagłówek <h/h1>  # Znacznik otwarcia i znacznik zamknięcia
<h2> nagłówek (mniejszy)
<a> anchor - kotwica, zakotwiczenie  # Tworzy hiperłącze
<br> break line
"""

"""
Paczki CSS:
Bootstrap 5

"""